from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "employee_data.db"

def execute_query(query: str, params=None):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    cursor = conn.cursor()

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return [dict(row) for row in rows]

if __name__ == "__main__":
    # Example usage
    query = "SELECT * FROM employees WHERE experience>=10;"
    result = execute_query(query)
    for row in result:
        print(row)
