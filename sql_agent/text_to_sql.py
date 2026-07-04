import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.ai.openai_client import client
from app.ai.prompt_builder import build_sql_prompt
from app.ai.response_parser import clean_sql
from config.settings import MODEL_NAME
from sql_agent.schema_service import get_database_schema


def generate_sql(question: str) -> str:
    schema = get_database_schema()
    prompt = build_sql_prompt(schema, question)
    response = client.responses.create(model=MODEL_NAME, input=prompt)
    return clean_sql(response.output_text)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = input("Enter a natural language prompt to generate SQL: ")
        if not question.strip():
            question = "Select employees with experience >= 10"

    print(generate_sql(question))
