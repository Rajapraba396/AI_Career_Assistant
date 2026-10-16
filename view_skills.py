from services.pdf_processor import extract_text_from_pdf
from services.text_processor import clean_text
from services.skill_extractor import extract_skills

pdf_path = "data/sample/resume.pdf"

raw_text = extract_text_from_pdf(pdf_path)
cleaned_text = clean_text(raw_text)
skills = extract_skills(cleaned_text)

print("===== EXTRACTED SKILLS =====")

if skills:
    for skill in skills:
        print("-", skill)
else:
    print("No matching skills found.")