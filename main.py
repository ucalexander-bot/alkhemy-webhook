from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return "Webhook is live!"
    elif request.method == "POST":
        data = request.get_json()
        print("Received GitHub webhook:", data)
        return jsonify({"status": "GitHub webhook received"}), 200
    else:
        return "Method not allowed", 405

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
