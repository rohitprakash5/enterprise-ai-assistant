#first_api.py
#fastapi learning 
#python -m uvicorn first_api:app --reload
#http://127.0.0.1:8000
#http://127.0.0.1:8000/docs
from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import csv
app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str
    experience: int

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    experience: Optional[int] = None  

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
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for emp in get_employee_data():
        if emp["id"] == employee_id:
            return emp
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )

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
    
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee_update: EmployeeUpdate):
    employees = get_employee_data()
    for emp in employees:
        if emp["id"] == employee_id:
            if employee_update.name is not None:
                emp["name"] = employee_update.name
            if employee_update.experience is not None:
                emp["experience"] = employee_update.experience
            with open("employee_fastapi.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["id", "name", "experience"])
                writer.writeheader()
                writer.writerows(employees)
            return {"message": "Employee updated successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    employees = get_employee_data()
    for emp in employees:
        if emp["id"] == employee_id:
            employees.remove(emp)
            with open("employee_fastapi.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["id", "name", "experience"])
                writer.writeheader()
                writer.writerows(employees)
            return {"message": "Employee deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )