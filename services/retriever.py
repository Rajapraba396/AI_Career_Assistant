
import numpy as np

from services.embeddings import generate_embedding
from services.vector_store import create_vector_store


def retrieve_relevant_text(query, texts, top_k=2):
    # Generate embeddings for the text collection
    embeddings = [generate_embedding(text) for text in texts]

    # Build the FAISS index
    index = create_vector_store(embeddings)

    # Convert the query into an embedding
    query_embedding = generate_embedding(query)

    query_vector = np.array(
        [query_embedding],
        dtype="float32"
    )

    # Search for the closest vectors
    k = min(top_k, len(texts))
    distances, indices = index.search(query_vector, k)

    # Return the matching original text
    results = []

    for i, position in enumerate(indices[0]):
        results.append({
            "text": texts[position],
            "distance": float(distances[0][i])
        })

    return results
