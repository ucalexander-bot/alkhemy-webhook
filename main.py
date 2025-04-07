from flask import Flask, request, jsonify
import requests
import os
import tempfile
import email
from email import policy

app = Flask(__name__)

@app.route('/')
def home():
    return 'Alkhemy Webhook is Live!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Check if attachment is included
    attachment_url = None
    for key, value in data.items():
        if isinstance(value, str) and "amazonaws.com" in value and value.endswith(".eml"):
            attachment_url = value
            break

    if not attachment_url:
        return jsonify({"status": "no attachment found"}), 400

    # Download the attachment
    try:
        response = requests.get(attachment_url)
        response.raise_for_status()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".eml") as tmp_file:
            tmp_file.write(response.content)
            tmp_path = tmp_file.name

        # Parse the .eml file
        with open(tmp_path, "rb") as f:
            msg = email.message_from_binary_file(f, policy=policy.default)
        
        subject = msg["subject"]
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break
        else:
            body = msg.get_payload(decode=True).decode()

        os.remove(tmp_path)  # cleanup temp file

        return jsonify({
            "status": "success",
            "subject": subject,
            "body": body[:500]  # return preview
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
