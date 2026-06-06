#first_api.py
#python -m uvicorn first_api:app --reload
#http://127.0.0.1:8000
#http://127.0.0.1:8000/docs
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import csv
app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str
    experience: int

def get_employee_data():
    employees = []
    with open("employee_fastapi.csv", "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if not row or not row.get("id"):
                continue
            try:
                row["id"] = int(row["id"])
            except (TypeError, ValueError):
                continue
            try:
                row["experience"] = int(row["experience"]) if row.get("experience") else 0
            except (TypeError, ValueError):
                row["experience"] = 0
            employees.append(row)
    return employees


#employees = [
#    {"id": 1, "name": "Rohit", "experience": 20},
#    {"id": 2, "name": "Amit", "experience": 10},
#    {"id": 3, "name": "Priya", "experience": 5}
#]

@app.get("/")
def read_root():
    return {"message": "Welcome to Rohit's First FastAPI Application"}

@app.get("/employees")
def read_employees():
    return get_employee_data()


@app.get("/senior-employees")
def get_senior_employees():
    
    senior_emps = [emp for emp in get_employee_data() if emp["experience"] >= 10]
    return senior_emps           


@app.get("/employees/count")
def count_employees():
    return {"count": len(get_employee_data())}

@app.get("/employees/filter")
def filter_employees(
    min_experience: Optional[int] = None
):
    employees = get_employee_data()
    if min_experience is None:
        return employees
    return [
        emp
        for emp in employees
        if emp["experience"] >= min_experience
    ]

@app.get("/employees/search/{name}")
def search_employee(name: str):

    for emp in get_employee_data():

        if emp["name"].lower() == name.lower():
            return emp

    return {"message": "Employee not found"}

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for emp in get_employee_data():
        if emp["id"] == employee_id:
            return emp
    return {"message": "Employee not found"}

@app.post("/employees")
def create_employee(employee: Employee):

    with open(
        "employee_fastapi.csv",
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            employee.id,
            employee.name,
            employee.experience
        ])

    return {
        "message": "Employee added successfully"
    }
    
