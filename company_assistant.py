from concurrent.futures import ThreadPoolExecutor

from planner.planner import create_plan
from sql_agent.agent import sql_agent
from rag_agent import rag_agent
from tool_agent import tool_agent
from app.ai.response_synthesizer import synthesize


AGENT_MAP = {
    "sql": sql_agent,
    "rag": rag_agent,
    "tool": tool_agent,
}


def _run_agent(step):
    agent = AGENT_MAP.get(step.agent)
    if not agent:
        return f"Unknown agent '{step.agent}' for question: {step.question}"

    try:
        return agent.answer_question(step.question)
    except Exception as exc:
        return f"Agent '{step.agent}' failed: {exc}"


def company_assistant(question: str):
    plan = create_plan(question)

    if not plan.steps:
        return "No plan steps were generated."

    max_workers = min(len(plan.steps), len(AGENT_MAP))
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        responses = list(executor.map(_run_agent, plan.steps))

    return synthesize(question, responses)


if __name__ == "__main__":
    answer = company_assistant(
        "How many employees do we have and what is the leave policy?"
    )
    print(answer)
