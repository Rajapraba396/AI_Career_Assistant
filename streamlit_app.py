
import streamlit as st
from services.rag_service import answer_question

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="💼",
    layout="centered"
)

st.title("AI Career Assistant")
st.write(
    "Ask questions about careers, skills, resumes, "
    "and interview preparation."
)


documents = [
    "Python developers use Python to build applications, automate tasks, and solve problems.",
    "Python developer skills include Python programming, object-oriented programming, SQL, and problem-solving.",
    "SQL is used by Python developers to retrieve, insert, update, and manage data in relational databases. It helps applications store and access user information, transactions, and other structured data.",
    "AI engineers work with machine learning, large language models, embeddings, and retrieval-augmented generation (RAG)."
]

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Accept a new question
question = st.chat_input("Ask a career question...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                history = st.session_state.messages[:-1]

                answer = answer_question(
                    question,
                    documents,
                    history
                )

                st.write(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as e:
                st.error("Unable to generate an answer.")
                st.caption(f"Error details: {e}")
