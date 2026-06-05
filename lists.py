tools = ["Informatica", "Snowflake", "Databricks", "LangChain"]

print(tools)

print(tools[0])
print(tools[1])

print("Learning:", tools[3])

tools.append("Python")
print(tools)

print("Number of tools:", len(tools))


tools = ["Informatica", "Snowflake", "Databricks", "LangChain", "Python"]

for tool in tools:
    print(tool)

years = [20, 5, 3, 1]

for year in years:
    print(f"experience: {year} years")