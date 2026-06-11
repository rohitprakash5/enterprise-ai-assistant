from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI( api_key=os.getenv("OPENAI_API_KEY") )

def ask_llm(question: str) -> str:
    response = client.responses.create(model="gpt-5",input= question)
    return response.output_text