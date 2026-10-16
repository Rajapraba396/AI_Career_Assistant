import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from services.skill_extractor import extract_skills


def test_extract_skills():
    text = """
    I know Python, SQL, Machine Learning, and FastAPI.
    I have also worked with GitHub.
    """

    skills = extract_skills(text)

    assert "Python" in skills
    assert "SQL" in skills
    assert "Machine Learning" in skills
    assert "FastAPI" in skills
    assert "GitHub" in skills