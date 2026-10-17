
from services.skill_extractor import extract_skills
from services.jd_analyzer import analyze_job_description


def match_resume_to_job(resume_text, job_description):
    resume_skills = extract_skills(resume_text)
    job_result = analyze_job_description(job_description)
    required_skills = job_result["required_skills"]

    matched_skills = [
        skill for skill in required_skills
        if skill in resume_skills
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in resume_skills
    ]

    if required_skills:
        match_percentage = (
            len(matched_skills) / len(required_skills)
        ) * 100
    else:
        match_percentage = 0.0

    return {
        "resume_skills": resume_skills,
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": round(match_percentage, 2),
    }
