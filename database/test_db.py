from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "employee_data.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('''select * from employees''')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
