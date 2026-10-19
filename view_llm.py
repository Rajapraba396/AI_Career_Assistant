
from services.llm_service import generate_response

prompt = """
Explain what a Python developer does in three simple sentences.
"""

answer = generate_response(prompt)

print("===== GEMINI RESPONSE =====")
print(answer)
