from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentence1 = "Employees receive 12 casual leaves per year."

sentence2 = "What is the leave policy?"

sentence3 = "How do I reset my laptop password?"

emb1 = model.encode([sentence1])
emb2 = model.encode([sentence2])
emb3 = model.encode([sentence3])

print(
    cosine_similarity(emb1, emb2)
)

print(
    cosine_similarity(emb1, emb3)
)