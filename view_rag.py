
from services.rag_service import answer_question

documents = [
    "Python developers build applications, write scripts, and automate tasks.",
    "SQL is used to store, retrieve, and manage data in databases.",
    "Machine learning engineers develop models that learn patterns from data.",
    "Communication skills help developers collaborate with team members."
]

question = "What is a Python developer's salary?"

answer = answer_question(question, documents)

print("===== RAG RESPONSE =====")
print(answer)
