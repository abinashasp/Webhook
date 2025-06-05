from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
import pytz

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/") 
db = client["webhookDB"]
events = db["events"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def github_webhook():
    data = request.json
    action_type = ""
    author = ""
    from_branch = ""
    to_branch = ""
    timestamp = datetime.utcnow().replace(tzinfo=pytz.utc).isoformat()

    # Push Event
    if "head_commit" in data:
        action_type = "push"
        author = data["pusher"]["name"]
        to_branch = data["ref"].split("/")[-1]

    # Pull Request Event
    elif "pull_request" in data:
        pr = data["pull_request"]
        action_type = "merge" if pr.get("merged") else "pull_request"
        author = pr["user"]["login"]
        from_branch = pr["head"]["ref"]
        to_branch = pr["base"]["ref"]

    else:
        return "Unsupported event", 400

    events.insert_one({
        "author": author,
        "action_type": action_type,
        "from_branch": from_branch,
        "to_branch": to_branch,
        "timestamp": timestamp
    })

    return jsonify({"status": "success"}), 200

@app.route('/events', methods=['GET'])
def get_events():
    data = list(events.find().sort("timestamp", -1))
    for d in data:
        d["_id"] = str(d["_id"])
    return jsonify(data)

