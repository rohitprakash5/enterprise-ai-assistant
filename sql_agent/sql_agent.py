import json
import sys
import time
import logging
from dataclasses import dataclass
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.ai.prompt_builder import build_sql_prompt, build_explanation_prompt
from app.ai.response_parser import clean_sql, parse_json
from config.business_rules import load_business_rules
from llm_service import generate as llm_generate
from sql_agent.schema_service import get_database_schema
from sql_agent.sql_service import execute_query as execute_sql_query

logger = logging.getLogger(__name__)


@dataclass
class SQLGenerationResult:
    sql: str
    reasoning: str


@dataclass
class AgentResponse:
    question: str
    sql: str
    reasoning: str
    rows: list[dict]
    answer: str
    business_rules: str
    execution_time: float


def generate_sql(question: str, business_rules: str | None = None) -> SQLGenerationResult:
    """Generate a SQLite SELECT statement and reasoning from a natural language question."""
    schema = get_database_schema()
    prompt = build_sql_prompt(schema, question, business_rules)
    response_text = llm_generate(prompt)
    payload = parse_json(response_text)
    sql = clean_sql(payload.get("sql", ""))
    reasoning = payload.get("reasoning", "")
    return SQLGenerationResult(sql=sql, reasoning=reasoning)


def explain_result(question: str, sql: str, rows: list[dict], business_rules: str | None = None) -> str:
    """Generate a business-friendly explanation of the SQL result rows."""
    if not rows:
        return "No results were returned for your question."

    prompt = build_explanation_prompt(question, sql, rows, business_rules)
    response_text = llm_generate(prompt)
    return response_text.strip()


def execute_query(sql: str, params=None) -> list[dict]:
    """Execute the generated SQL against the SQLite database and return rows."""
    return execute_sql_query(sql, params)


def answer_question(question: str, business_rules: str | None = None) -> AgentResponse:
    """Full pipeline: question -> SQL -> rows -> business answer."""
    if business_rules is None:
        business_rules = load_business_rules()

    start_time = time.perf_counter()
    logger.info("Generating SQL")
    result = generate_sql(question, business_rules)
    logger.info("SQL generated: %s", result.sql)

    logger.info("Executing SQL")
    rows = execute_query(result.sql)
    logger.info("Rows returned: %d", len(rows))

    logger.info("Generating explanation")
    answer = explain_result(question, result.sql, rows, business_rules)

    execution_time = time.perf_counter() - start_time
    logger.info("Total Time: %.3f sec", execution_time)

    return AgentResponse(
        question=question,
        sql=result.sql,
        reasoning=result.reasoning,
        rows=rows,
        answer=answer,
        business_rules=business_rules,
        execution_time=execution_time,
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = input("Enter a natural language question: ")

    answer = answer_question(question)
    logger.info("Generated Answer:\n%s", answer)
