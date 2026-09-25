import os
from flask import Flask, request, jsonify
from groq import Groq

app = Flask(__name__)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

@app.route("/", methods=["GET"])
def home():
    return "Groq AI Chatbot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful and friendly AI assistant."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        bot_reply = response.choices[0].message.content

        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
