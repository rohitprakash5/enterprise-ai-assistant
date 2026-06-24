from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

BASE_DIR = Path(__file__).parent
CHROMA_PATH = BASE_DIR / "chroma_db"

model = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.PersistentClient( path=str(CHROMA_PATH))

collection = chroma_client.get_collection(
    "company_docs"
)
def ask_hr_policy(question):
    question_embedding = model.encode(
        question
    ).tolist()
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3
    )

    print("\nRetrieved Documents:")
    print(results["documents"])

    print("\nSource:")
    print(results["metadatas"])

    context = "\n".join(
        results["documents"][0]
    )

    prompt = f"""
Answer the question using only the context below.

Context:

{context}

Question:

{question}
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text

print(
    ask_hr_policy(
        "How many casual leaves can I take?"
    )
)
#
#User Question
#       ↓
#    Router
#       ↓
# ┌───────────────┬───────────────┐
# │               │               │
#Tool          RAG Search      GPT
# │               │               │
# └───────────────┴───────────────┘
#       ↓
#   Final Answer