
from services.llm_service import generate_response


def generate_interview_questions(
    job_role,
    skills,
    num_questions=5,
    difficulty="Beginner",
    include_answers=False
):
    skills_text = ", ".join(skills)

    if include_answers:
        answer_instruction = """
For every question, provide a simple, accurate sample answer.
Keep each answer concise and suitable for interview preparation.
"""
    else:
        answer_instruction = "Generate questions only. Do not provide answers."

    prompt = f"""
You are an experienced technical interviewer.

Generate {num_questions} interview questions.

Job role: {job_role}
Skills: {skills_text}
Difficulty: {difficulty}

Requirements:
1. Match the questions to the job role and skills.
2. Follow the requested difficulty level.
3. Include practical, role-relevant questions.
4. Number each question.
5. {answer_instruction}

Use clear, professional language.
"""

    return generate_response(prompt)
