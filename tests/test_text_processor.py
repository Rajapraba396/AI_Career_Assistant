import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from services.text_processor import clean_text


def test_clean_text():
    text = "   Python     SQL    Machine Learning   "

    cleaned_text = clean_text(text)

    assert cleaned_text == "Python SQL Machine Learning"