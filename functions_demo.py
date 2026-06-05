def classify_employee(name, experience):

    if experience >= 10:
        return f"{name} is a Senior Employee"

    else:
        return f"{name} is a Junior Employee"


print(classify_employee("Rohit", 20))
print(classify_employee("Priya", 5))

employees = [
    {"name": "Rohit", "experience": 20},
    {"name": "Amit", "experience": 10},
    {"name": "Priya", "experience": 5}
]

for emp in employees:
    print(classify_employee(emp["name"], emp["experience"]))