import json


def build_sql_prompt(schema: str, question: str, business_rules: str | None = None) -> str:
    rules = """
Rules:
1. Only generate SQLite SQL
2. Only SELECT statements
3. Never INSERT
4. Never UPDATE
5. Never DELETE
6. Never DROP
7. Never ALTER
8. Return SQL only
"""

    business_section = ""
    if business_rules:
        business_section = f"\nBusiness Rules:\n{business_rules}\n"

    return f"""
You are an expert SQL developer.

{rules}{business_section}
Database Schema:
{schema}

Question:
{question}

If the question refers to senior or junior employees, apply the business rules above.

Return only valid JSON with these keys:
- sql: the SQLite SELECT statement
- reasoning: the short reasoning for the generated SQL
"""


def build_explanation_prompt(question: str, sql: str, rows: list[dict], business_rules: str | None = None) -> str:
    """Build the prompt used to explain query results in natural language."""
    rows_text = json.dumps(rows, indent=2)
    rules_section = ""
    if business_rules:
        rules_section = f"Business Rules\n{business_rules}\n"

    return (
        "You are an HR assistant.\n"
        f"{rules_section}"
        f"Generated SQL:\n{sql}\n"
        f"Database Result:{rows_text}\n"
        f"User Question:{question}\n"
        "Explain using ONLY the business rules, generated SQL, and returned rows."
    )
