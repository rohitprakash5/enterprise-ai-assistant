employees = [
    {"name": "Rohit", "experience": 20},
    {"name": "Amit", "experience": 10},
    {"name": "Priya", "experience": 5}
]

def get_experienced_band(experience):
    if experience >= 15:
        return "Expert"
    elif experience >= 10:
        return "Senior"
    elif experience >= 5:
        return "Mid-Level"
    else:
        return "Junior"

for emp in employees:
    emp["band"] = get_experienced_band(emp["experience"])
for emp in employees:
   print(f"{emp['name']} -> {emp['band']}")

print(employees[0])

