# rag/embedder.py

from sentence_transformers import SentenceTransformer

# Load embedding model once
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed_text(text: str):
    """Embed a single text string."""
    return model.encode(text).tolist()

def embed_list(text_list):
    """Embed a list of strings."""
    return model.encode(text_list).tolist()
