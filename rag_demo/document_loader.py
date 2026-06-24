from pathlib import Path
BASE_DIR = Path(__file__).parent



def load_document(file_path):
    file_path = BASE_DIR / file_path
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
text = load_document("hr_policy.txt")

#print(text)

def chunk_text(text):
    chunks = text.split("\n")
    return [
        chunk.strip()
        for chunk in chunks
        if chunk.strip()
    ]
#def chunk_text(text):
#    chunks= text.split("\n\n")
#    return [chunk.strip() for chunk in chunks if chunk.strip()]
    
chunks = chunk_text(text)
#for chunk in chunks:
#    print(chunk)
#    print("-----")
