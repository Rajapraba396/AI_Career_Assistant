
from services.retriever import retrieve_relevant_text
from services.llm_service import generate_response


def answer_question(question, documents, chat_history=None):
    if chat_history is None:
        chat_history = []

    # Step 1: Build a query using the previous conversation
    retrieval_query = question
    
    # Step 2: Retrieve relevant documents
    results = retrieve_relevant_text(
        retrieval_query,
        documents,
        top_k=2
    )

    # Step 3: Combine retrieved text
    context = "\n".join(
        result["text"] for result in results
    )

    # Step 4: Format conversation history
    history = "\n".join(
        f"{item['role']}: {item['content']}"
        for item in chat_history
    )

    # Step 5: Build the prompt
    prompt = f"""
You are an AI career assistant.

Use the context and conversation history to answer.
Answer using the provided context.
If the information is unavailable, say you do not have enough information.

Context:
{context}

Previous conversation:
{history}

Current question:
{question}

Give a clear, simple answer.
"""

    # Step 6: Generate the response
    return generate_response(prompt)
