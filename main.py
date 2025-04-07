from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello from Alkhemy Webhook!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render assigns PORT env variable
    app.run(host="0.0.0.0", port=port)
