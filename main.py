import json
from flask import Flask, request, abort
import hmac
import hashlib
import os

app = Flask(__name__)
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET").encode()

@app.route("/", methods=["POST"])
def webhook():
    # Validate GitHub signature
    signature = request.headers.get('X-Hub-Signature-256')
    if not signature:
        abort(400, "No signature found")

    sha_name, signature = signature.split('=')
    mac = hmac.new(WEBHOOK_SECRET, msg=request.data, digestmod=hashlib.sha256)
    if not hmac.compare_digest(mac.hexdigest(), signature):
        abort(403, "Invalid signature")

    # Log the payload to a file
    payload = request.get_json()
    with open("webhook_log.json", "a") as f:
        json.dump(payload, f)
        f.write("\n")  # Add a newline between entries

    return "OK", 200
