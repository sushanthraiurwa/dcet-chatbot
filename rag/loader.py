import pdfplumber
import os

PDF_FOLDER = "data"   # folder containing all PDFs

def extract_all_pdfs():
    print("Extracting all PDFs...")
    full_text = ""

    for file in os.listdir(PDF_FOLDER):
        if file.lower().endswith(".pdf"):
            pdf_path = os.path.join(PDF_FOLDER, file)
            print("Reading:", pdf_path)

            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        full_text += text + "\n"

    return full_text


def chunk_text(text, chunk_size=500):
    chunks = []
    current = 0
    while current < len(text):
        chunk = text[current : current + chunk_size].strip()
        chunks.append(chunk)
        current += chunk_size
    return chunks


def load_documents():
    full_text = extract_all_pdfs()
    chunks = chunk_text(full_text)

    print("Total chunks:", len(chunks))
    return chunks
