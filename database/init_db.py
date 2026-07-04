from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "employee_data.db"

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    experience INTEGER NOT NULL
)''')

employees = [
      (1, "Rohit", 20),
    (2, "Amit", 10),
    (3, "Priya", 5),
    (4, "Raj", 9),
    (5, "Rahul", 8)
    ]

cursor.executemany('''
INSERT OR REPLACE INTO employees (id, name, experience) 
                   VALUES (?, ?, ?)'''
                   , employees)

conn.commit()
conn.close()

print("Database created successfully!")