employee = {
    "name": "Rohit",
    "experience": 20,
    "tool": "Informatica",
    "cloud": "Snowflake"
}

print(employee)

print(employee["name"])
print(employee["tool"])

employee["ai_topic"] = "LangChain"
print(employee)

profile = {
     "name": "Rohit",
    "experience": 20,
    "primary_tool": "Informatica",
    "snowflake_certified": True,
    "learning_now": "LangChain"
    }
print(profile)

employees = [
    {"name": "Rohit", "tool": "Informatica"},
    {"name": "Amit", "tool": "Snowflake"},
    {"name": "Priya", "tool": "Databricks"}
]

for employee in employees:
    print(employee["name"])


employees = [
    {"name": "Rohit", "experience": 20},
    {"name": "Amit", "experience": 10},
    {"name": "Priya", "experience": 5}
]

for employee in employees:
    print(f"{employee['name']} has {employee['experience']} years of experience.")