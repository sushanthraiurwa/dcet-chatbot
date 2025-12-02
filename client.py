import requests

API_URL = "http://127.0.0.1:8000/ask"

print("=== DCET Chatbot ===")

while True:
    question = input("You: ")

    if question.lower() in ["exit", "quit"]:
        print("Bot: Bye bro ❤️")
        break

    response = requests.post(API_URL, json={"question": question})

    try:
        data = response.json()

        answer = data.get("answer", None)

        if isinstance(answer, str):
            print("\n📌 Bot Answer:\n")
            print(answer)
            print("\n" + "-"*60 + "\n")
        else:
            print("Bot:", data)

    except:
        print("Bot: Error decoding response")
