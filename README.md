# 📰 Ranchi Watch

An automated Python-based RSS news monitoring system for Ranchi that filters important news, prevents duplicate alerts, and sends real-time notifications using **ntfy**.

## ✨ Features

- 📡 Fetches news from multiple RSS feeds
- 🎯 Keyword-based filtering
- 🚨 Severity classification
  - 🔴 High
  - 🟠 Medium
  - 🟢 Low
- 📱 Instant notifications via ntfy
- 🚫 Duplicate detection using `seen_links.txt`
- ☁️ Runs automatically every 5 hours with GitHub Actions
- 🔄 Automatically updates processed links

---

## 📂 Project Structure

```
ranchi-watch/
│
├── .github/
│   └── workflows/
│       └── ranchi-watch.yml
│
├── app.py
├── config.py
├── requirements.txt
├── seen_links.txt
│
├── sources/
│   └── rss.py
│
├── utils/
│   └── notifier.py
│
└── README.md
```

---

## ⚙️ Tech Stack

- Python 3.11+
- feedparser
- requests
- schedule
- GitHub Actions
- ntfy

---

## 🚀 How It Works

```text
GitHub Actions
        │
        ▼
Runs every 5 hours
        │
        ▼
Fetch RSS News
        │
        ▼
Filter by Keywords
        │
        ▼
Check Duplicate Links
        │
        ▼
Assign Severity
        │
        ▼
Send Notification
        │
        ▼
Update seen_links.txt
```

---

## 🔔 Severity Levels

| Severity | Description |
|----------|-------------|
| 🔴 HIGH | Critical incidents, cyber attacks, murders, Naxal activities, etc. |
| 🟠 MEDIUM | CID investigations, accidents, arrests, fraud, etc. |
| 🟢 LOW | Government updates and general news |

---

## 📱 Notifications

Example:

```
🚨 Ranchi Watch

Top Relevant News

1. Headline
Link

2. Headline
Link
```

---

## 🔄 Automation

The project is powered by **GitHub Actions**.

Every workflow:

- Fetches latest RSS news
- Filters relevant headlines
- Sends ntfy notification
- Updates processed links
- Pushes updated `seen_links.txt`

No local computer is required after deployment.

---

## 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/flickshot-bit/ranchi-watch.git
```

Move into the project:

```bash
cd ranchi-watch
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
python app.py
```

---

## 📌 Future Improvements

- AI-generated news summaries
- Multi-city monitoring
- Telegram integration
- Email alerts
- Discord webhook support
- Web dashboard
- Sentiment analysis

---

## 👨‍💻 Author

**Aditya Kumar**

GitHub:
https://github.com/flickshot-bit

---

## ⭐ If you found this project useful

Give this repository a ⭐ on GitHub.
