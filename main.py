from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or request.form or {}
    print("📬 Webhook received!")
    print("📦 Payload:", data)

    return jsonify({"status": "received"}), 200
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
