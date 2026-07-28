SEEN_FILE = "seen_links.txt"

from utils.notifier import send_notification
from config import (
    RSS_FEEDS,
    MAX_HEADLINES,
    KEYWORDS,
    HIGH_SEVERITY,
    MEDIUM_SEVERITY,
    LOW_SEVERITY,
)
from sources.rss import fetch_news

import schedule
import time


def is_relevant(title):
    title = title.lower()
    return any(keyword.lower() in title for keyword in KEYWORDS)


def load_seen_links():
    try:
        with open(SEEN_FILE, "r", encoding="utf-8") as file:
            return set(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        return set()


def save_seen_link(link):
    with open(SEEN_FILE, "a", encoding="utf-8") as file:
        file.write(link + "\n")


def get_severity(title):
    text = title.lower()

    if any(word in text for word in HIGH_SEVERITY):
        return "🔴 HIGH"

    if any(word in text for word in MEDIUM_SEVERITY):
        return "🟠 MEDIUM"

    if any(word in text for word in LOW_SEVERITY):
        return "🟢 LOW"

    return "⚪ INFO"


def main():
    seen_links = load_seen_links()
    alerts = []

    print("=" * 60)
    print("📰 Ranchi Watch Started")
    print("=" * 60)

    for feed in RSS_FEEDS:
        try:
            articles = fetch_news(feed)

            print(f"\nFound {len(articles)} articles\n")

            for index, article in enumerate(articles[:MAX_HEADLINES], start=1):
                text = f"{article['title']} {article.get('summary', '')}"

                if not is_relevant(text):
                    continue

                if article["link"] in seen_links:
                    continue

                severity = get_severity(article["title"])

                print(f"\n#{index}")
                print(f"{severity} {article['title']}")
                print(article["link"])
                print("-" * 60)

                if severity in ["🔴 HIGH", "🟠 MEDIUM"]:
                    save_seen_link(article["link"])
                    seen_links.add(article["link"])

                    alerts.append(
                        {
                            "title": article["title"],
                            "link": article["link"],
                        }
                    )

        except Exception as e:
            print(f"Error reading feed: {e}")

    if alerts:
        message = "Top 5 Relevant News\n\n"

        for i, alert in enumerate(alerts[:5], start=1):
            message += (
                f"{i}. {alert['title']}\n"
                f"{alert['link']}\n\n"
            )

        if len(alerts) > 5:
            message += f"...and {len(alerts) - 5} more news."

        send_notification("🚨 Ranchi Watch", message)

    else:
        print("\nNo relevant news found.")


if __name__ == "__main__":
    main()