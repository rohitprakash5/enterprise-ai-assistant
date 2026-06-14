import chromadb
from pathlib import Path
from sentence_transformers import SentenceTransformer
import document_loader

BASE_DIR = Path(__file__).parent
CHROMA_PATH = BASE_DIR / "chroma_db"
model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_or_create_collection(name="hr_policy")

text = document_loader.load_document("hr_policy.txt")
chunks = document_loader.chunk_text(text)

for i, chunk in enumerate(chunks):
    embedding = model.encode(chunk).tolist()
    collection.add(
        ids=[str(i)],
        documents=[chunk],
        embeddings=[embedding]
    )

print("Index Built")    