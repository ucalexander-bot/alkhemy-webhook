from flask import Flask, request, jsonify
import json
import datetime

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    now = datetime.datetime.now().isoformat()

    # Print to terminal
    print(f"\n[Webhook received @ {now}]\n{json.dumps(data, indent=2)}\n")

    # Optional: Save to file
    with open("webhook_log.json", "a") as f:
        f.write(f"\n[Webhook received @ {now}]\n")
        f.write(json.dumps(data, indent=2))
        f.write("\n")

    return jsonify({"status": "received"}), 200
