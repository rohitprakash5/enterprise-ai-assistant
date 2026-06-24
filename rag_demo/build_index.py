import chromadb
from pathlib import Path
from sentence_transformers import SentenceTransformer
import document_loader
from pdf_loader import load_pdf

BASE_DIR = Path(__file__).parent
DOC_DIR = BASE_DIR / "documents"
pdf_files = DOC_DIR.glob("*.pdf")
CHROMA_PATH = BASE_DIR / "chroma_db"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=str(CHROMA_PATH))

try:
    client.delete_collection("company_docs")
except:
    pass
collection = client.get_or_create_collection("company_docs")

#collection = client.get_or_create_collection("company_docs")

for pdf_file in pdf_files:
    print("Processing:", pdf_file.name)
    text = load_pdf(pdf_file)
    chunks = document_loader.chunk_text(text)
    for i, chunk in enumerate(chunks):
        embedding = model.encode(chunk).tolist()
        collection.add(
            ids=[f"{pdf_file.stem}_{i}"],
            documents=[chunk],
            embeddings=[embedding],
            metadatas=[
                {
                    "source": pdf_file.name
                }
            ]
        )

print("Index Built")