from flask import Flask, request
import logging
import json

app = Flask(__name__)

# Set logging level
logging.basicConfig(level=logging.INFO)

@app.route("/", methods=["POST"])
def webhook():
    payload = request.get_json()

    # Pretty-print the JSON payload to Render logs
    app.logger.info("🔔 Webhook received:\n%s", json.dumps(payload, indent=2))

    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
