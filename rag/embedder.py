import onnxruntime as ort
from transformers import AutoTokenizer
import numpy as np

# ----------------------------
# LOAD TOKENIZER
# ----------------------------
tokenizer = AutoTokenizer.from_pretrained("models/all-MiniLM-L6-v2")


# ----------------------------
# LOAD ONNX MODEL
# ----------------------------
session = ort.InferenceSession("models/all-MiniLM-L6-v2.onnx")
def embed_text(text):
    # Tokenize text
    inputs = tokenizer(
        text,
        return_tensors="np",
        truncation=True,
        max_length=256,
        padding="max_length"
    )

    # Some models require token_type_ids → fix here
    if "token_type_ids" not in inputs:
        inputs["token_type_ids"] = np.zeros_like(inputs["input_ids"])

    # Run ONNX
    outputs = session.run(None, {
        "input_ids": inputs["input_ids"],
        "attention_mask": inputs["attention_mask"],
        "token_type_ids": inputs["token_type_ids"]
    })

    # Mean Pooling
    emb = np.mean(outputs[0], axis=1)[0]
    return emb.tolist()


def embed_list(texts):
    embeddings = []
    for t in texts:
        embeddings.append(embed_text(t))
    return embeddings
