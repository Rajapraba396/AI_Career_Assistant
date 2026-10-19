
from services.interview_generator import generate_interview_questions


def test_generate_interview_questions(monkeypatch):
    def fake_generate_response(prompt):
        return "1. What is Python?\n2. Explain OOP."

    monkeypatch.setattr(
        "services.interview_generator.generate_response",
        fake_generate_response
    )

    result = generate_interview_questions(
        job_role="Python Developer",
        skills=["Python", "OOP"],
        num_questions=2
    )

    assert "What is Python?" in result
    assert "Explain OOP." in result


def test_generate_questions_with_answers(monkeypatch):
    def fake_generate_response(prompt):
        return "1. What is Python?\nAnswer: Python is a programming language."

    monkeypatch.setattr(
        "services.interview_generator.generate_response",
        fake_generate_response
    )

    result = generate_interview_questions(
        job_role="Python Developer",
        skills=["Python"],
        num_questions=1,
        include_answers=True
    )

    assert "What is Python?" in result
    assert "Answer:" in result
