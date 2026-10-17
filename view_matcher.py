
from services.pdf_processor import extract_text_from_pdf
from services.text_processor import clean_text
from services.matcher import match_resume_to_job

# Read the sample resume
resume_text = extract_text_from_pdf("data/sample/resume.pdf")
resume_text = clean_text(resume_text)

# Example job description
job_description = """
We are looking for a candidate with Python, SQL, FastAPI,
Machine Learning, Git, and Communication skills.
"""

# Match the resume with the job description
result = match_resume_to_job(resume_text, job_description)

print("===== RESUME-JOB MATCHING RESULT =====")
print("Resume skills:", result["resume_skills"])
print("Required skills:", result["required_skills"])
print("Matched skills:", result["matched_skills"])
print("Missing skills:", result["missing_skills"])
print("Match percentage:", result["match_percentage"], "%")
