from openai import OpenAI
from dotenv import load_dotenv
import os
import services
#services.py is a module that contains functions to interact with the employee data stored 
# in a CSV file. It provides functions to get employee data, save new employees, count employees,
#  and get senior employee count. The llm_service.py module uses these functions to provide 
# higher-level functionalities like asking questions to the LLM and providing 
# employee-related advice based on the data.

load_dotenv()
client = OpenAI( api_key=os.getenv("OPENAI_API_KEY") )

def ask_llm(question: str) -> str:
    response = client.responses.create(model="gpt-5",input= question)
    return response.output_text

def employee_advisor(question: str) -> str:
    print("CALLING GPT")
    employees = services.get_employee_data()
    prompt = f"""
You are an HR assistant.

Business Rules:
- Senior Employee = experience >= 10
- Junior Employee = experience < 10

Employee Data:

{employees}

Answer the following question:

{question}
"""
    response = client.responses.create(  model="gpt-5", input=prompt)
    return response.output_text

#def employee_agent(question: str):
    question_lower = question.lower()
    if "how many senior employees" in question_lower:
        result = services.get_senior_employee_count()
        return f"There are {result} senior employees in the company."
    if "how many" in question_lower and "employees" in question_lower:
        result = services.count_employees()
        return f"There are {result} employees in the company."
    if "most experienced" in question_lower:
        emp = services.get_most_experienced_employee()
    return (
        f"{emp['name']} is the most experienced "
        f"employee with {emp['experience']} years."
    )
    return employee_advisor(question)

def employee_agent(question: str):
    question_lower = question.lower()
    if "how many senior employees" in question_lower:
        print("TOOL USED: get_senior_employee_count")
        result = services.get_senior_employee_count()
        return f"There are {result} senior employees."
    if "how many" in question_lower and "employees" in question_lower:
        print("TOOL USED: count_employees")
        result = services.count_employees()
        return f"There are {result} employees."
    if "most experienced" in question_lower:
        print("TOOL USED: get_most_experienced_employee")
        emp = services.get_most_experienced_employee()
        return (
            f"{emp['name']} is the most experienced employee "
            f"with {emp['experience']} years."
        )
    print("TOOL USED: GPT FALLBACK")
    return employee_advisor(question)    