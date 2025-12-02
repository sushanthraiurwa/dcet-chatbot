# rag/retriever.py

import chromadb
from chromadb.config import Settings
from rag.loader import load_documents
from rag.embedder import embed_text, embed_list

# Create persistent Chroma folder
chroma = chromadb.PersistentClient(path="vector_store")

# Create or load vector collection
collection = chroma.get_or_create_collection(
    name="dcet_rag",
    metadata={"hnsw:space": "cosine"}  # cosine similarity
)


def build_index():
    print("🔥 Building DCET Index...")
    docs = load_documents()  # extract + chunk PDFs
    ids = [f"chunk_{i}" for i in range(len(docs))]

    print("🔥 Generating embeddings...")
    embeddings = embed_list(docs)  # LOCAL embeddings (ONNX)

    # Clear old collection
    existing = collection.get()
    if existing and existing.get("ids"):
        print("🗑️ Clearing old data...")
        collection.delete(ids=existing["ids"])

    print("📥 Adding new documents to ChromaDB...")
    collection.add(
        documents=docs,
        ids=ids,
        embeddings=embeddings
    )

    print("✅ Index built successfully!")


def search(query, k=3):
    query_emb = embed_text(query)  # LOCAL embed text

    results = collection.query(
        query_embeddings=[query_emb],
        n_results=k
    )

    return results
