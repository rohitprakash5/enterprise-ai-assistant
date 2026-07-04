from agent_base import BaseAgent
from llm_service import ask_llm


class ToolAgent(BaseAgent):
    def answer_question(self, question: str) -> str:
        """Answer a question using the general tool/GPT agent."""
        prompt = f"Answer the question using tools and available knowledge:\n\nQuestion:\n{question}"
        return ask_llm(prompt)


tool_agent = ToolAgent()
