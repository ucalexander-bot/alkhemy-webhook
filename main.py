from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/")
async def handle_webhook(request: Request):
    payload = await request.json()

    repo = payload.get("repository", {}).get("full_name", "Unknown repo")
    pusher = payload.get("pusher", {}).get("name", "Someone")
    commits = payload.get("commits", [])

    commit_messages = [commit.get("message", "No message") for commit in commits]
    summary = f"📦 Push to {repo} by {pusher}\n"
    summary += "\n".join([f"- {msg}" for msg in commit_messages])

    print("\n🔔 GitHub Push Summary:\n" + summary + "\n")

    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
