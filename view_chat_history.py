
from services.rag_service import answer_question

documents = [
    "Python developers build applications, write scripts, and automate tasks.",
    "SQL is used to store, retrieve, and manage data in databases.",
    "Machine learning engineers develop models that learn patterns from data."
]

# Store the conversation in a list
chat_history = []

# First question
question1 = "What does a Python developer do?"
answer1 = answer_question(
    question1, documents, chat_history
)

print("User:", question1)
print("Assistant:", answer1)

# Save the first conversation
chat_history.append({
    "role": "user",
    "content": question1
})
chat_history.append({
    "role": "assistant",
    "content": answer1
})

# Follow-up question
question2 = "Which programming language does that developer use?"
answer2 = answer_question(
    question2, documents, chat_history
)

print("\nUser:", question2)
print("Assistant:", answer2)
