import json

with open("employee_data.json", "r") as file:
    employees = json.load(file)

print(employees)

for emp in employees:
    print(emp["name"])

for emp in employees:
    if emp["experience"] >= 10:
        print(emp["name"])