
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from services.retriever import retrieve_relevant_text


def test_retrieve_relevant_text():
    texts = [
        "I develop machine learning models.",
        "I build web applications using Python and FastAPI.",
        "I analyze data using SQL and Pandas.",
        "I enjoy cooking food and trying new recipes."
    ]

    results = retrieve_relevant_text(
        "What experience do I have with AI?",
        texts,
        top_k=2
    )

    assert len(results) == 2
    assert all("text" in result for result in results)
    assert all("distance" in result for result in results)
