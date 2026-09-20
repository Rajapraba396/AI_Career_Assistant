import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from services.pdf_processor import extract_text_from_pdf
from services.text_processor import clean_text


def test_resume_cleaning():
    raw_text = extract_text_from_pdf("data/sample/resume.pdf")

    cleaned_text = clean_text(raw_text)

    assert cleaned_text is not None
    assert len(cleaned_text) > 0