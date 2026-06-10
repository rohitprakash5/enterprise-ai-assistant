# main.py

from typing import Optional

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from models import Employee
from models import EmployeeUpdate

from services import (
    get_employee_data,
    save_employee,
    update_employee_service,
    delete_employee_service
)

app = FastAPI()


@app.get("/")
def read_root():

    return {
        "message": "Welcome to Rohit's First FastAPI Application"
    }


@app.get("/employees")
def read_employees():

    return get_employee_data()


@app.get("/employees/count")
def count_employees():

    return {
        "count": len(get_employee_data())
    }


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

    return save_employee(employee)


@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    employee_update: EmployeeUpdate
):

    return update_employee_service(
        employee_id,
        employee_update
    )


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    return delete_employee_service(
        employee_id
    )