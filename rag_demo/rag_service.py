import chromadb
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

model = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.Client()
#collection = chroma_client.create_collection("hr_policy")
try:
    collection = chroma_client.get_collection(
        "hr_policy"
    )
except:
    collection = chroma_client.create_collection(
        "hr_policy"
    )

documents = [
    "Employees receive 12 casual leaves per year.",
    "Employees are eligible for medical insurance after 90 days.",
    "Work from home is allowed up to 3 days per week.",
    "Travel expenses must be approved by the manager."
]

for i,doc in enumerate(documents):
    embedding = model.encode(doc).tolist()
    
    collection.add(
    ids=[str(i)],
    documents=[doc],
    embeddings=[embedding]
    )

#print("Documents loaded into Chroma.")

def ask_hr_policy(question):
    question_embedding = model.encode(question).tolist()
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=1
    )
    #print(results)
    print("\nRetrieved Context:")
    print(results["documents"][0][0])

    print("\nDistance:")
    print(results["distances"][0][0])

    context = results["documents"][0][0]

      
    prompt = f"""Answer the question using only the context below.
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