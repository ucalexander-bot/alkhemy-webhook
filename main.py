from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        print("Webhook received!")
        print(request.json)
        return "Webhook received!", 200
    else:
        return "Hello from Alkhemy Webhook!", 200

if __name__ == "__main__":
    app.run(debug=True)
