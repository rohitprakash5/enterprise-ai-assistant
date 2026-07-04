from agent_base import BaseAgent
from rag_demo.rag_service import ask_hr_policy


class RAGAgent(BaseAgent):
    def answer_question(self, question: str) -> str:
        """Answer a question using the RAG service."""
        return ask_hr_policy(question)


rag_agent = RAGAgent()
