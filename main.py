from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/", methods=["POST"])
def webhook():
    # Log raw headers and body for debugging
    print("Webhook received!")
    print(request.headers)
    print(request.get_data())

    # Example response
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
