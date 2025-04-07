from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or request.form or {}
    print("📬 Webhook received!")
    print("📦 Payload:", data)

    return jsonify({"status": "received"}), 200
