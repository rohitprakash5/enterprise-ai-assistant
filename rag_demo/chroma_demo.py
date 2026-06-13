import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.create_collection("hr_policy")

documents = [
    "Employees receive 12 casual leaves per year.",
    "Employees are eligible for medical insurance after 90 days.",
    "Work from home is allowed up to 3 days per week.",
    "Travel expenses must be approved by the manager."
]

for i , doc in enumerate(documents):
    embedding = model.encode(doc).tolist()
    
    collection.add(
    ids=[str(i)],
    documents=[doc],
    embeddings=[embedding]
    )

print("Documents loaded into Chroma.")

question = "How many casual leaves do employees receive?"
question_embedding = model.encode(question).tolist()
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=4
)
print(results["documents"])
print(results["distances"])