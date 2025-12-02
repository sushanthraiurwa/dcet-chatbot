from fastembed import TextEmbedding

embedder = TextEmbedding()

def embed_text(text: str):
    return list(embedder.embed([text]))[0]

def embed_list(texts: list):
    return list(embedder.embed(texts))
