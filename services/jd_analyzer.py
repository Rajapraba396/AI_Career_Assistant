
from services.skill_extractor import extract_skills


def analyze_job_description(job_description):
    skills = extract_skills(job_description)

    result = {
        "required_skills": skills,
        "total_skills_found": len(skills),
    }

    return result
