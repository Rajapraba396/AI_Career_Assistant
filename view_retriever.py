
from services.retriever import retrieve_relevant_text

texts = [
    "I develop machine learning models.",
    "I build web applications using Python and FastAPI.",
    "I analyze data using SQL and Pandas.",
    "I enjoy cooking food and trying new recipes."
]

query = "What experience do I have with AI?"

results = retrieve_relevant_text(query, texts, top_k=2)

print("Query:", query)
print("\nRetrieved text:")

for result in results:
    print("-", result["text"])
    print("  Distance:", round(result["distance"], 4))
