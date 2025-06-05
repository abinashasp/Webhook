# 📡 GitHub Webhook Receiver + Activity Dashboard

This project is a Flask-based application that receives GitHub webhook events (`push`, `pull_request`, and `merge`) from a separate GitHub repository and displays them in a clean UI. The received data is stored in MongoDB and fetched every 15 seconds to display live activity.

---

## 📁 Repositories

- **Source Repo (action):** [GitHub Repository](https://github.com/your-username/action)  
  _(Contains the GitHub Actions that trigger webhook events)_

- **Webhook Repo (this project):** [GitHub Repository](https://github.com/your-username/webhook)  
  _(Contains the webhook endpoint, MongoDB logic, and UI)_

---

## 🧩 Features

- Receives webhook events from GitHub:
  - `push`
  - `pull_request`
  - `merge` (if applicable)
- Stores event data in MongoDB
- Minimal frontend UI using HTML & JavaScript
- Polls the server every 15 seconds to update event list

---

## 🔧 Technologies Used

- **Backend:** Flask (Python)
- **Database:** MongoDB
- **Frontend:** HTML, JavaScript
- **Other Tools:** GitHub Webhooks, ngrok (for local testing)

---

## 📌 Webhook Payload Format

Stored format in MongoDB:

```json
{
  "author": "Travis",
  "action_type": "push",
  "from_branch": "staging",
  "to_branch": "master",
  "timestamp": "2021-06-04T10:00:00Z"
}
