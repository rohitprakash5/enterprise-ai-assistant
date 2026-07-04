import json
import os
import sys
from pathlib import Path

# Ensure the repository root is on sys.path when running this module directly.
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from .planner_prompt import build_planner_prompt
from .planner_models import PlannerResponse, PlannerStep
import llm_service


def create_plan(question: str) -> PlannerResponse:
    """Create a plan for answering the question using available agents."""
    prompt = build_planner_prompt(question)
    response = llm_service.generate(prompt)
    plan_json = json.loads(response)

    steps_data = []
    if isinstance(plan_json, dict):
        steps_data = plan_json.get("steps", [])

    steps: list[PlannerStep] = []
    if isinstance(steps_data, list):
        for step_data in steps_data:
            if not isinstance(step_data, dict):
                continue
            agent = str(step_data.get("agent", "")).strip().lower()
            question_text = str(step_data.get("question", "")).strip()
            if not agent or not question_text:
                continue
            steps.append(PlannerStep(agent=agent, question=question_text))

    return PlannerResponse(steps=steps)

#if __name__ == "__main__":
#    print(
#        create_plan(
#            "Who are senior employees and what is leave policy?"
#        )
#    )