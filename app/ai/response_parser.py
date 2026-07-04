import json
import re


def clean_sql(output: str) -> str:
    sql = output.strip()
    sql = re.sub(r"^```(?:sql)?\s*", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```$", "", sql).strip()

    match = re.search(r"((?:SELECT|WITH)\b[\s\S]*)",
                      sql,
                      flags=re.IGNORECASE)
    if match:
        sql = match.group(1).strip()

    sql = sql.rstrip()
    if sql.endswith(";"):
        return sql

    if ";" in sql:
        return sql[: sql.rfind(";") + 1]

    return sql


def parse_json(output: str) -> dict:
    payload = output.strip()
    payload = re.sub(r"^```(?:json)?\s*", "", payload, flags=re.IGNORECASE)
    payload = re.sub(r"```$", "", payload).strip()

    try:
        return json.loads(payload)
    except json.JSONDecodeError:
        match = re.search(r"\{[\s\S]*\}", payload)
        if match:
            return json.loads(match.group(0))
        raise
