
from services.interview_generator import generate_interview_questions

print("===== AI CAREER ASSISTANT =====")
print("1. Python Developer")
print("2. AI Engineer")
print("3. Data Analyst")
print("4. Software Developer")

roles = {
    "1": {
        "name": "Python Developer",
        "skills": ["Python", "OOP", "SQL", "Problem-solving"]
    },
    "2": {
        "name": "AI Engineer",
        "skills": ["Python", "Machine Learning", "LLMs", "RAG"]
    },
    "3": {
        "name": "Data Analyst",
        "skills": ["SQL", "Python", "Excel", "Data Visualization"]
    },
    "4": {
        "name": "Software Developer",
        "skills": ["Python", "OOP", "Data Structures", "Algorithms"]
    }
}

choice = input("\nChoose a job role (1-4): ").strip()

if choice not in roles:
    print("Invalid choice. Please select a number from 1 to 4.")
else:
    selected_role = roles[choice]

    difficulty = input(
        "Choose difficulty (Beginner / Intermediate / Advanced): "
    ).strip().title()

    if difficulty not in ["Beginner", "Intermediate", "Advanced"]:
        print("Invalid difficulty level.")
    else:
        questions = generate_interview_questions(
            job_role=selected_role["name"],
            skills=selected_role["skills"],
            num_questions=5,
            difficulty=difficulty,
            include_answers=True
        )

        print("\n===== INTERVIEW QUESTIONS =====")
        print("Role:", selected_role["name"])
        print("Difficulty:", difficulty)
        print("Skills:", ", ".join(selected_role["skills"]))
        print()
        print(questions)
