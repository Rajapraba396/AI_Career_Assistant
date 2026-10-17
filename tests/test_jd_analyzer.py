
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from services.jd_analyzer import analyze_job_description


def test_analyze_job_description():
    job_description = """
    We are looking for a Python Developer.
    Required skills: Python, SQL, Flask, REST API, and Git.
    """

    result = analyze_job_description(job_description)

    assert "Python" in result["required_skills"]
    assert "SQL" in result["required_skills"]
    assert "Flask" in result["required_skills"]
    assert result["total_skills_found"] == len(result["required_skills"])
