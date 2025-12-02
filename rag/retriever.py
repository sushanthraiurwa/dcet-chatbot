# rag/retriever.py

import chromadb
from chromadb.config import Settings
from rag.loader import load_documents
from rag.embedder import embed_list, embed_text

# Create persistent DB folder
chroma = chromadb.PersistentClient(
    path="vector_store",
    settings=Settings()
)

collection = chroma.get_or_create_collection(
    name="nmeo_rag",
    metadata={"hnsw:space": "cosine"}
)

def build_index():
    print("Building index from PDF chunks...")

    docs = load_documents()
    ids = [f"chunk_{i}" for i in range(len(docs))]
    embeddings = embed_list(docs)

    # Delete old data safely
    existing = collection.get()
    if existing and "ids" in existing and len(existing["ids"]) > 0:
        collection.delete(ids=existing["ids"])

    # Add new embeddings
    collection.add(
        documents=docs,
        ids=ids,
        embeddings=embeddings
    )

    print("Index built successfully!")


def search(query, k=3):
    query_embedding = embed_text(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results
