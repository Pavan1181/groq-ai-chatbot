import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("ERROR: GROQ_API_KEY not found.")
    exit()

client = Groq(api_key=api_key)

messages = [
    {
        "role": "system",
        "content": "You are a helpful and friendly AI assistant."
    }
]

print("==============================")
print("       GROQ AI CHATBOT")
print("==============================")
print("Type 'exit' to stop.")
print()

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("Bot: Goodbye bro!")
        break

    messages.append({
        "role": "user",
        "content": user_message
    })

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages
        )

        bot_reply = response.choices[0].message.content

        print("Bot:", bot_reply)
        print()

        messages.append({
            "role": "assistant",
            "content": bot_reply
        })

    except Exception as e:
        print("Error:", e)