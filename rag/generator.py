import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "llama3-70b-8192"  # correct Groq model name


def generate_answer(context, question):
    if not context:
        return "I can only answer questions based on the DCET PDF documents."

    combined = "\n\n".join(context[:5])

    system_prompt = (
        "You are a helpful DCET exam assistant. "
        "Use ONLY the provided context below. "
        "If the answer is not found in the context, say 'I don't know based on the PDF'."
    )

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Context:\n{combined}\n\nQuestion: {question}"}
            ]
        )

        return response.choices[0].message["content"]

    except Exception as e:
        return f"Error: {str(e)}"
