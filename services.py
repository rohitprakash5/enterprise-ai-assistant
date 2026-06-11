# services.py

import csv
from urllib import response
import requests
from fastapi import HTTPException, status


CSV_FILE = "employee_fastapi.csv"


def get_employee_data():

    employees = []

    with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if not row or not row.get("id"):
                continue

            try:
                row["id"] = int(row["id"])
            except (TypeError, ValueError):
                continue

            try:
                row["experience"] = (
                    int(row["experience"])
                    if row.get("experience")
                    else 0
                )
            except (TypeError, ValueError):
                row["experience"] = 0

            employees.append(row)

    return employees


def save_employee(employee):

    with open(CSV_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            employee.id,
            employee.name,
            employee.experience
        ])

    return {
        "message": "Employee added successfully"
    }


def update_employee_service(
    employee_id,
    employee_update
):

    employees = get_employee_data()

    for emp in employees:

        if emp["id"] == employee_id:

            if employee_update.name is not None:
                emp["name"] = employee_update.name

            if employee_update.experience is not None:
                emp["experience"] = employee_update.experience

            with open(CSV_FILE, "w", newline="") as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=["id", "name", "experience"]
                )

                writer.writeheader()
                writer.writerows(employees)

            return {
                "message": "Employee updated successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )


def delete_employee_service(employee_id):

    employees = get_employee_data()

    for emp in employees:

        if emp["id"] == employee_id:

            employees.remove(emp)

            with open(CSV_FILE, "w", newline="") as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=["id", "name", "experience"]
                )

                writer.writeheader()
                writer.writerows(employees)

            return {
                "message": "Employee deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )

def get_external_users():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()
        #return response.json()
        users = response.json()
        transformed_users = []
        
        for user in users:
            transformed_users.append({
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "company": user["company"]["name"]
            })
        return transformed_users
    except requests.RequestException as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"External service error: {str(exc)}"
        )
