
from services.chat_service import CareerChat


def test_chat_saves_user_and_assistant_messages(monkeypatch):
    def fake_answer_question(question, documents, chat_history):
        return f"Test answer for: {question}"

    monkeypatch.setattr(
        "services.chat_service.answer_question",
        fake_answer_question
    )

    assistant = CareerChat(["Python developers build applications."])

    answer = assistant.chat("What does a Python developer do?")

    assert answer == "Test answer for: What does a Python developer do?"
    assert len(assistant.chat_history) == 2
    assert assistant.chat_history[0]["role"] == "user"
    assert assistant.chat_history[1]["role"] == "assistant"


def test_chat_preserves_history_between_questions(monkeypatch):
    def fake_answer_question(question, documents, chat_history):
        return f"Test answer for: {question}"

    monkeypatch.setattr(
        "services.chat_service.answer_question",
        fake_answer_question
    )

    assistant = CareerChat(["Python developers build applications."])

    assistant.chat("What does a Python developer do?")
    assistant.chat("Which language does that developer use?")

    assert len(assistant.chat_history) == 4
    assert assistant.chat_history[2]["role"] == "user"
    assert assistant.chat_history[3]["role"] == "assistant"
