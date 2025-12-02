from rag.retriever import build_index

if __name__ == "__main__":
    build_index()

# from groq import Groq
# import os

# from openai import OpenAI
# from dotenv import load_dotenv


# load_dotenv()

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# models = client.models.list()

# for m in models.data:
#     print(m.id)

# client = OpenAI(api_key="", base_url="https://api.groq.com/openai/v1")
# print(client.embeddings.create(model="nomic-embed-text-v1", input="hello"))
