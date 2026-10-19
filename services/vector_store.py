
import faiss
import numpy as np


def create_vector_store(embeddings):
    # Convert embeddings to a NumPy array
    vectors = np.array(embeddings, dtype="float32")

    # Get the number of dimensions in each vector
    dimension = vectors.shape[1]

    # Create a FAISS index for similarity search
    index = faiss.IndexFlatL2(dimension)

    # Add vectors to the index
    index.add(vectors)

    return index
