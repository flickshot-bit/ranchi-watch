import feedparser


def fetch_news(url):
    feed = feedparser.parse(url)

    articles = []

    for item in feed.entries:
        articles.append({
            "title": item.title,
            "link": item.link
        })

    return articles