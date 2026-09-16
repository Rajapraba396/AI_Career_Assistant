import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from services.pdf_processor import extract_text_from_pdf


def test_pdf_extraction():
    text = extract_text_from_pdf("data/sample/resume.pdf")

    assert text is not None
    assert len(text) > 0