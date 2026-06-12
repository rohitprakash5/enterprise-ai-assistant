# main.py

from typing import Optional

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

import models

import llm_service

import services

app = FastAPI()


@app.get("/")
def read_root():

    return {
        "message": "Welcome to Rohit's First FastAPI Application"
    }


@app.get("/employees")
def read_employees():

    return services.get_employee_data()


@app.get("/employees/count")
def count_employees():

    return {
        "count": len(services.get_employee_data())
    }


@app.get("/employees/filter")
def filter_employees(
    min_experience: Optional[int] = None
):

    employees = services.get_employee_data()

    if min_experience is None:
        return employees

    return [
        emp
        for emp in employees
        if emp["experience"] >= min_experience
    ]


@app.get("/employees/search/{name}")
def search_employee(name: str):

    for emp in services.get_employee_data():

        if emp["name"].lower() == name.lower():
            return emp

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    for emp in services.get_employee_data():

        if emp["id"] == employee_id:
            return emp

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )


@app.post("/employees")
def create_employee(employee: models.Employee):

    return services.save_employee(employee)


@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    employee_update: models.EmployeeUpdate
):

    return services.update_employee_service(
        employee_id,
        employee_update
    )


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    return services.delete_employee_service(
        employee_id
    )

@app.get("/external-users")
def get_external_users():
    return services.get_external_users()


@app.post("/ask")
def ask_gpt(request: models.QuestionRequest):
    answer = llm_service.ask_llm(request.question)
    return {
        "question": request.question,
        "answer": answer
    }

@app.post("/advisor")
def get_advice(request: models.AdvisorRequest):
    answer = llm_service.employee_advisor(request.question)
    return {
        "question": request.question,
        "answer": answer
    }

@app.post("/employee-agent")
def ask_employee_agent(request: models.AdvisorRequest):
    answer = llm_service.employee_agent(request.question)
    return {
        "question": request.question,
        "answer": answer
    }