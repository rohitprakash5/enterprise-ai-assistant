from dataclasses import dataclass

@dataclass
class PlannerStep:
    """Represents a single step in the planning process."""
    agent: str
    question: str
  
@dataclass
class PlannerResponse:
    """Represents the response from the planner."""
    steps: list[PlannerStep]
