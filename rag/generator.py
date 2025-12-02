import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "llama-3.3-70b-versatile"   # BEST free Groq model


def generate_answer(context, question):
    if not context:
        return "I can only answer questions based on the DCET PDF documents."

    combined = "\n\n".join(context[:5])

    system_prompt = (
        "You are a helpful DCET exam assistant. "
        "Use ONLY the provided context below. "
        "If the answer is not found in the context, say you don't know."
    )

    try:
        response = client.responses.create(
            model=MODEL,
            input=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": f"CONTEXT:\n{combined}\n\nQUESTION: {question}"
                }
            ]
        )

        return response.output_text

    except Exception as e:
        return f"Error: {str(e)}"
