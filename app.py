from flask import Flask, request, render_template, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}]
    )
    bot_message = response.choices[0].message["content"]
    return jsonify({"response": bot_message})

if __name__ == "__main__":
    app.run(debug=True)