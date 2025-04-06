from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Webhook is live!"

@app.route("/api/summarize-email", methods=["POST"])
def summarize_email():
    data = request.get_json()
    subject = data.get("subject", "")
    body = data.get("body", "")

    summary = f'Summary of email: Subject is "{subject}" and body is approximately {len(body)} characters long.'
    return jsonify({"summary": summary})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
