
from services.retriever import retrieve_relevant_text
from services.llm_service import generate_response


def answer_question(question, documents, chat_history=None):
    if chat_history is None:
        chat_history = []

    # Step 1: Retrieve relevant documents
    results = retrieve_relevant_text(
        question,
        documents,
        top_k=2
    )

    # Step 2: Build the context
    context = "\n".join(
        result["text"] for result in results
    )

    # Step 3: Include previous conversation
    history = "\n".join(
        f"{item['role']}: {item['content']}"
        for item in chat_history
    )

    # Step 4: Create the prompt
    prompt = f"""
You are an AI career assistant.

Use the context and conversation history to answer.
Prefer the provided context for factual information.
If the information is unavailable, say so.

Context:
{context}

Previous conversation:
{history}

Current question:
{question}

Give a clear, simple answer.
"""

    # Step 5: Generate the response
    return generate_response(prompt)
