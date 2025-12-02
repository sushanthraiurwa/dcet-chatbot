from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

from rag.retriever import search
from rag.generator import generate_answer

# --------------------------
# CREATE APP + ENABLE CORS
# --------------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # Allow All Frontends
    allow_credentials=True,
    allow_methods=["*"],            # ENABLE OPTIONS METHOD
    allow_headers=["*"],
)

# --------------------------
# REQUEST BODY MODEL
# --------------------------
class Question(BaseModel):
    question: str

# --------------------------
# /ask ROUTE
# --------------------------
@app.post("/ask")
def ask_question(question: Optional[str] = Query(None), body: Optional[Question] = None):

    # Priority for body JSON
    if body and body.question:
        question_text = body.question
    else:
        question_text = question

    if not question_text:
        return {"error": "No question provided"}

    # Vector search
    results = search(question_text, k=3)
    docs = results["documents"][0] if results.get("documents") else []

    # LLM answer
    answer = generate_answer(docs, question_text)

    return {"answer": answer}
