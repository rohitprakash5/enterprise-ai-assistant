from openai import OpenAI
from dotenv import load_dotenv
import os
from services import get_employee_data

load_dotenv()
client = OpenAI( api_key=os.getenv("OPENAI_API_KEY") )

def ask_llm(question: str) -> str:
    response = client.responses.create(model="gpt-5",input= question)
    return response.output_text

def employee_advisor(question: str) -> str:
    employees = get_employee_data()
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