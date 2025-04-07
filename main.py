from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    payload = request.get_json()
    timestamp = datetime.utcnow().isoformat()

    print("\n✅ Webhook received at", timestamp)
    print(json.dumps(payload, indent=2))

    # Optional: write to file
    with open("webhook_log.json", "a") as f:
        f.write(f"\n=== {timestamp} ===\n")
        f.write(json.dumps(payload, indent=2))
        f.write("\n\n")

    return jsonify({"status": "received"}), 200
