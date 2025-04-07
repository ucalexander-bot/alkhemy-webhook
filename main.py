from flask import Flask, request
import os
import hmac
import hashlib

app = Flask(__name__)

WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "supersecretvalue123")  # Same as GitHub

def verify_signature(payload, signature):
    mac = hmac.new(WEBHOOK_SECRET.encode(), msg=payload, digestmod=hashlib.sha256)
    expected = "sha256=" + mac.hexdigest()
    return hmac.compare_digest(expected, signature)

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        signature = request.headers.get("X-Hub-Signature-256", "")
        if not verify_signature(request.data, signature):
            print("⚠️ Invalid signature!")
            return "Invalid signature", 403

        print("✅ Webhook received!")
        print(request.json)
        return "Webhook received!", 200
    else:
        return "Hello from Alkhemy Webhook!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
