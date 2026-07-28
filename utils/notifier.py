import requests

TOPIC = "ranchiwatch5954"

def send_notification(title, message):
    response = requests.post(
        f"https://ntfy.sh/{TOPIC}",
        data=message.encode("utf-8"),
        timeout=10
    )

    print("Status:", response.status_code)
    print("Response:", response.text)