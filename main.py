from flask import Flask, request, jsonify

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
