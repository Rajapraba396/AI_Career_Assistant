
from services.rag_service import answer_question


class CareerChat:
    def __init__(self, documents):
        self.documents = documents
        self.chat_history = []

    def chat(self, question):
        # Generate an answer using RAG and conversation history
        answer = answer_question(
            question,
            self.documents,
            self.chat_history
        )

        # Save the user's question
        self.chat_history.append({
            "role": "user",
            "content": question
        })

        # Save the assistant's answer
        self.chat_history.append({
            "role": "assistant",
            "content": answer
        })

        return answer
