
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from services.embeddings import generate_embedding


def test_generate_embedding():
    text = "I develop machine learning models."

    embedding = generate_embedding(text)

    assert embedding is not None
    assert len(embedding) == 384
