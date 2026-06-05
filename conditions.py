employees = [
    {"name": "Rohit", "experience": 20},
    {"name": "Amit", "experience": 10},
    {"name": "Priya", "experience": 5}
]

for emp in employees:
     if emp["experience"] >= 10:
        print(f"{emp['name']} is a senior employee with {emp['experience']} years of experience.")
     else:
        print(f"{emp['name']} is a junior employee with {emp['experience']} years of experience.")