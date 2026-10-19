
from fastapi import FastAPI
from pydantic import BaseModel, Field
from services.rag_service import answer_question


class CareerQuestion(BaseModel):
    question: str = Field(min_length=1, max_length=1000)


documents = [
    "Python developers use Python to build applications, automate tasks, and solve problems.",
    "Python developer skills include Python programming, object-oriented programming, SQL, and problem-solving.",
    "AI engineers work with machine learning, large language models, embeddings, and retrieval-augmented generation (RAG)."
]

app = FastAPI(
    title="AI Career Assistant",
    description="An API for AI-powered career assistance",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to my AI Career Assistant API!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Career Assistant"
    }


@app.post("/ask")
def ask_career_question(data: CareerQuestion):
    answer = answer_question(
        data.question,
        documents
    )

    return {
        "question": data.question,
        "answer": answer
    }

