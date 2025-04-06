from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return "Webhook is live!"
    elif request.method == "POST":
        data = request.get_json()
        print("Received GitHub webhook:", data)
        return jsonify({"status": "GitHub webhook received"}), 200

@app.route("/api/summarize-email", methods=["POST"])
def summarize_email():
    data = request.get_json()
    subject = data.get("subject", "")
    body = data.get("body", "")
    summary = f"Summary of email: Subject is '{subject}' and body is approximately {len(body)} characters long."
    return jsonify({"summary": summary})

# 🔧 This line ensures the app binds to the correct port on Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
