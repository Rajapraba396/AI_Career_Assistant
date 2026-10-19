
from services.chat_service import CareerChat

documents = [
    "Python developers build applications, write scripts, and automate tasks.",
    "SQL is used to store, retrieve, and manage data in databases.",
    "Machine learning engineers develop models that learn patterns from data.",
    "Communication skills help developers collaborate with team members.",
    "A resume should clearly present skills, projects, education, and experience."
]

assistant = CareerChat(documents)

questions = [
    "What does a Python developer do?",
    "What database language is useful for managing data?",
    "Why are communication skills important?",
    "What should I include in my resume?",
    "What is the salary of a Python developer?"
]

for question in questions:
    print("\nUser:", question)
    answer = assistant.chat(question)
    print("Assistant:", answer)

print("\nTotal messages:", len(assistant.chat_history))
