
from services.jd_analyzer import analyze_job_description

job_description = """
We are looking for a Python Developer.
Required skills: Python, SQL, Flask, REST API, and Git.
Experience with Machine Learning and FastAPI is an advantage.
"""

result = analyze_job_description(job_description)

print("===== JOB DESCRIPTION ANALYSIS =====")
print("Skills found:", result["required_skills"])
print("Total skills found:", result["total_skills_found"])
