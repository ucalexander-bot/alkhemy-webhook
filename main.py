from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key (you can also use an env variable)
openai.api_key = os.getenv("OPENAI_API_KEY") or "sk-..."

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return "Webhook is live!"
    
    elif request.method == "POST":
        data = request.get_json()
        print("Received GitHub webhook:", data)

        # Build a commit summary prompt
        commits = data.get("commits", [])
        commit_messages = "\n".join(f"- {c['message']} by {c['author']['name']}" for c in commits)

        prompt = (
            "Summarize the following GitHub commit activity in plain language:\n"
            f"{commit_messages}"
        )

        # Send to OpenAI for summary
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant who summarizes GitHub commit activity."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )

            summary = response.choices[0].message["content"]
            print("Summary:", summary)
            return jsonify({"summary": summary}), 200

        except Exception as e:
            print("OpenAI error:", e)
            return jsonify({"error": "Failed to generate summary"}), 500

    else:
        return "Method not allowed", 405
