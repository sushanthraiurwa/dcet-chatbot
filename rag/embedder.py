from fastembed import TextEmbedding

embedder = TextEmbedding()

def embed_text(text: str):
    # embed returns generator → convert to list → take first
    return list(embedder.embed([text]))[0]

def embed_list(texts: list):
    # convert generator to list
    return list(embedder.embed(texts))
