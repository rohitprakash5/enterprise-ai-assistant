import services
from rag_demo.rag_service import ask_hr_policy
from llm_service import ask_llm

def company_assistant(question):
    question_lower = question.lower()
    context =""
    
    if ("employee" in question_lower
        or "people" in question_lower
        or "workforce" in question_lower):
        total_employees = services.count_employees()
        context += (f"Total employees: {total_employees}\n")
    if "leave" in question_lower:
        leave_policy = ask_hr_policy(question)
        context += (f"Leave policy: {leave_policy}\n")
    if "experience" in question_lower:
        average_experience = services.get_average_experience()
        context += (f"Average experience: {average_experience}\n")
    if "most experienced" in question_lower:
        most_experienced = (   services.get_most_experienced_employee() )
        context += (
        f"Most experienced employee: "
        f"{most_experienced['name']} "
        f"with {most_experienced['experience']} years\n"
        )

    prompt = f"""
Answer using the information below.
{context}
Question:
{question}
"""
    return ask_llm(prompt)

print(
    company_assistant(
        "How many employees do we have and what is the leave policy?"
    )
)