
import re


SKILL_LIST = [
    # Programming and software
    "Python",
    "Java",
    "C++",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "Flask",
    "FastAPI",
    "REST API",
    "Git",
    "GitHub",

    # AI and data science
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Data Analysis",
    "Data Visualization",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",
    "Computer Vision",
    "Natural Language Processing",
    "Generative AI",
    "Large Language Models",
    "RAG",

    # Business and communication
    "Sales",
    "Communication",
    "Negotiation",
    "Customer Service",
    "Customer Relationship Management",
    "Marketing",
    "Business Development",
    "Teamwork",
    "Leadership",
    "Problem Solving",
    "Time Management",
    "Project Management",

    # Operations and logistics
    "Inventory Management",
    "Warehouse Management",
    "Logistics",
    "Supply Chain Management",
    "Quality Control",
    "Record Keeping",
    "Cleaning Equipment",
    "Deep Sanitation Practices",
    "Mathematics",
]


def extract_skills(text):
    found_skills = []

    for skill in SKILL_LIST:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills
