from pathlib import Path
from pypdf import PdfReader


BASE_DIR = Path(__file__).parent

def load_pdf(file_name):
    pdf_path = BASE_DIR / file_name
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text



text = load_pdf("sample_policy.pdf")
print(text[:500])