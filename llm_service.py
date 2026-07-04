import logging
import services
from app.ai.openai_client import client
from config.settings import MODEL_NAME

# services.py is a module that contains functions to interact with the employee data stored
# in a CSV file. It provides functions to get employee data, save new employees, count employees,
# and get senior employee count. The llm_service.py module uses these functions to provide
# higher-level functionalities like asking questions to the LLM and providing
# employee-related advice based on the data.

logger = logging.getLogger(__name__)


def generate(prompt: str, model: str = MODEL_NAME) -> str:
    response = client.responses.create(model=model, input=prompt)
    return response.output_text


def ask_llm(question: str) -> str:
    response = client.responses.create(model=MODEL_NAME, input=question)
    return response.output_text

def employee_advisor(question: str) -> str:
    logger.info("CALLING GPT")
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
    response = client.responses.create(model=MODEL_NAME, input=prompt)
    return response.output_text

def employee_agent(question: str):
    question_lower = question.lower()
    if "how many senior employees" in question_lower:
        logger.info("TOOL USED: get_senior_employee_count")
        result = services.get_senior_employee_count()
        return f"There are {result} senior employees."
    if "how many" in question_lower and "employees" in question_lower:
        logger.info("TOOL USED: count_employees")
        result = services.count_employees()
        return f"There are {result} employees."
    if "most experienced" in question_lower:
        logger.info("TOOL USED: get_most_experienced_employee")
        emp = services.get_most_experienced_employee()
        return (
            f"{emp['name']} is the most experienced employee "
            f"with {emp['experience']} years."
        )
    logger.info("TOOL USED: GPT FALLBACK")
    return employee_advisor(question)


tools = [
    {
        "type": "function",
        "name": "count_employees",
        "description": "Returns total number of employees"
    },
    {
        "type": "function",
        "name": "get_employee_names",
        "description": "Returns a list of all employee names"
    },
    {
        "type": "function",
        "name": "get_average_experience",
        "description": "Returns the average experience of all employees"
    },
    {
    "type": "function",
    "name": "workforce_summary",
    "description": "Returns a workforce summary including employee count, average experience and most experienced employee"
}
]


def employee_agent_v2(question: str):
    response = client.responses.create(
        model=MODEL_NAME,
        input=question,
        tools=tools
    )
    tool_call = response.output[1]
    logger.info("Tool selected: %s", tool_call.name)
    logger.info(tool_call.name)
    if tool_call.name == "count_employees":
       result = services.count_employees()
       return f"There are {result} employees."
    if tool_call.name == "get_employee_names":
       names = services.get_employee_names()
       return ", ".join(names)
    if tool_call.name == "get_average_experience":
        avg = services.get_average_experience()
        return f"Average experience is {avg} years."
    if tool_call.name == "workforce_summary":
        summary = services.workforce_summary()
        return (
        f"Total Employees: {summary['total']}, "
        f"Average Experience: {summary['average']} years, "
        f"Most Experienced Employee: "
        f"{summary['top_employee']} "
        f"({summary['top_experience']} years)"
        )
    return "No tool matched"


