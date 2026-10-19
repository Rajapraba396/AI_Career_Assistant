
from services.embeddings import generate_embedding
from services.vector_store import create_vector_store

texts = [
    "I develop machine learning models.",
    "I build web applications using Python and FastAPI.",
    "I analyze data using SQL and Pandas.",
    "I enjoy cooking food and trying new recipes."
]

# Generate embeddings for all texts
embeddings = [generate_embedding(text) for text in texts]

# Create the vector store
index = create_vector_store(embeddings)

# Search query
query = "I want to learn about artificial intelligence."

# Convert the query into an embedding
query_embedding = generate_embedding(query)

# Search for the two closest vectors
distances, indices = index.search(
    query_embedding.reshape(1, -1).astype("float32"),
    2
)

print("Search query:", query)
print("\nMost relevant results:")

for i, index_position in enumerate(indices[0]):
    print(f"\n{i + 1}. {texts[index_position]}")
    print(f"   Distance: {distances[0][i]:.4f}")
