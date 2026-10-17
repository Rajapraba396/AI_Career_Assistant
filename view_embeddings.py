
from services.embeddings import generate_embedding
from sklearn.metrics.pairwise import cosine_similarity

sentence1 = "I develop machine learning models."
sentence2 = "I enjoy cooking food and trying new recipes."

embedding1 = generate_embedding(sentence1)
embedding2 = generate_embedding(sentence2)

similarity = cosine_similarity(
    [embedding1],
    [embedding2]
)[0][0]

print("Sentence 1:", sentence1)
print("Sentence 2:", sentence2)
print("Semantic similarity:", round(float(similarity), 4))
