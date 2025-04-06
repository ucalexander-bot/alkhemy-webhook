from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Webhook is live!"

@app.route("/github", methods=["POST"])
def github_webhook():
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
