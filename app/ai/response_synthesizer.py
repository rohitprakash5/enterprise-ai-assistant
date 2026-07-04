from llm_service import ask_llm


def synthesize(question: str, responses: list[str]) -> str:
    """Synthesize a final answer from multiple agent responses."""
    if not responses:
        return "No agent responses were available to synthesize."

    joined_responses = "\n\n".join(
        f"Response {idx + 1}: {resp}" for idx, resp in enumerate(responses)
    )

    prompt = f"""
You are a response synthesizer. A user asked the following question:

{question}

Multiple agents produced the following responses:

{joined_responses}

Produce one final, concise answer in a single paragraph.
Use the available information only. If the question is about employee count or leave policy, include those facts.
Format key numeric facts and leave entitlements in markdown bold (for example, **5 employees**, **12 casual leaves per year**).
Do not include either the agent names or step details in the final answer.
Example output:
The company currently has **5 employees**. According to the HR policy, employees are entitled to **12 casual leaves per year**, and unused leave cannot be carried forward.
"""

    return ask_llm(prompt).strip()
