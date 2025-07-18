import feedparser
from datetime import datetime, timezone

def fetch_skift():
    url = "https://skift.com/feed/"
    feed = feedparser.parse(url)
    articles = []

    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'url': entry.link,
            'published': datetime(*entry.published_parsed[:6], tzinfo=timezone.utc),
            'source': "Skift"
        })
    return articles

def fetch_phocuswire():
    url = "https://www.phocuswire.com/rss"
    feed = feedparser.parse(url)
    articles = []

    # Defensive check for RSS validity
    if not feed.entries or not hasattr(feed.entries[0], 'published_parsed'):
        return []

    for entry in feed.entries:
        try:
            articles.append({
                'title': entry.title,
                'url': entry.link,
                'published': datetime(*entry.published_parsed[:6], tzinfo=timezone.utc),
                'source': "PhocusWire"
            })
        except Exception:
            continue
    return articles


