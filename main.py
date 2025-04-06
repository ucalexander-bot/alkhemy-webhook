from flask import Flask, request, jsonify
import os

app = Flask(__name__)

print("🚀 Flask server started and ready!")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return "Webhook is live!"
    elif request.method == "POST":
        print("📩 POST request received at '/'")
        try:
            data = request.get_json()
            print("✅ Received GitHub webhook data:", data)
            return jsonify({"status": "GitHub webhook received"}), 200
        except Exception as e:
            print("❌ Error parsing JSON from webhook:", str(e))
            return jsonify({"error": "Failed to parse JSON"}), 400

@app.route("/api/summarize-email", methods=["POST"])
def summarize_email():
    data = request.get_json()
    subject = data.get("subject", "")
    body = data.get("body", "")
    summary = f"Summary of email: Subject is '{subject}' and body is approximately {len(body)} characters long."
    return jsonify({"summary": summary})
