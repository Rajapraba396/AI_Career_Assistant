
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == (
        "Welcome to my AI Career Assistant API!"
    )


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_ask_rejects_empty_question():
    response = client.post(
        "/ask",
        json={"question": ""}
    )
    assert response.status_code == 422


def test_ask_rejects_long_question():
    response = client.post(
        "/ask",
        json={"question": "a" * 1001}
    )
    assert response.status_code == 422


def test_ask_returns_answer(monkeypatch):
    def fake_answer_question(question, documents):
        return "Python developers build applications using Python."

    monkeypatch.setattr(
        "main.answer_question",
        fake_answer_question
    )

    response = client.post(
        "/ask",
        json={
            "question": "What does a Python developer do?"
        }
    )

    assert response.status_code == 200
    assert response.json()["question"] == (
        "What does a Python developer do?"
    )
    assert response.json()["answer"] == (
        "Python developers build applications using Python."
    )
