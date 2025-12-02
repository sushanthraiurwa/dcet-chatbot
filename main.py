from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional

from rag.retriever import search
from rag.generator import generate_answer

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_question(question: Optional[str] = Query(None), body: Optional[Question] = None):
    # Priority: body > query
    if body and body.question:
        question_text = body.question
    else:
        question_text = question

    if not question_text:
        return {"error": "No question provided"}

    results = search(question_text, k=3)
    docs = results["documents"][0] if results.get("documents") else []

    answer = generate_answer(docs, question_text)

    return {"answer": answer}
