from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DEFAULT_BUSINESS_RULES = """Senior Employee:
experience >= 10

Junior Employee:
experience < 10
"""


def load_business_rules(path: str | None = None) -> str:
    if path:
        file_path = Path(path)
        if file_path.exists():
            return file_path.read_text().strip()

    for candidate in [ROOT_DIR / "business_rules.txt", ROOT_DIR / "business_rules.md"]:
        if candidate.exists():
            return candidate.read_text().strip()

    return DEFAULT_BUSINESS_RULES
