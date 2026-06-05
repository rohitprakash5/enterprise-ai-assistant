import json

employee_json = """
{
    "name": "Rohit",
    "experience": 20,
    "tool": "Informatica"
}
"""

employee = json.loads(employee_json)

print(employee)

print(employee["name"])
print(employee["tool"])