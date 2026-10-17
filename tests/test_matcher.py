
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from services.matcher import match_resume_to_job


def test_match_resume_to_job():
    resume_text = """
    I know Python, SQL, Git, and Machine Learning.
    """

    job_description = """
    We need Python, SQL, FastAPI, and Machine Learning.
    """

    result = match_resume_to_job(resume_text, job_description)

    assert "Python" in result["matched_skills"]
    assert "SQL" in result["matched_skills"]
    assert "FastAPI" in result["missing_skills"]
    assert result["match_percentage"] == 75.0
