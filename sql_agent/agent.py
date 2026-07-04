from agent_base import BaseAgent
from sql_agent.sql_agent import answer_question as sql_answer_question


class SQLAgent(BaseAgent):
    def answer_question(self, question: str) -> str:
        response = sql_answer_question(question)
        return response.answer if hasattr(response, "answer") else str(response)


sql_agent = SQLAgent()
