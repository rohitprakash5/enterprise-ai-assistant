from abc import ABC, abstractmethod


class BaseAgent(ABC):
    @abstractmethod
    def answer_question(self, question: str) -> str:
        """Answer a natural language question."""
        raise NotImplementedError
