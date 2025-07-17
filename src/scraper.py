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

def fetch_google_news():
    url = "https://news.google.com/rss/search?q=travel+technology"
    feed = feedparser.parse(url)
    articles = []

    for entry in feed.entries:
        published = entry.get("published_parsed") or entry.get("updated_parsed")
        published_dt = datetime(*published[:6], tzinfo=timezone.utc) if published else datetime.utcnow().replace(tzinfo=timezone.utc)
        articles.append({
            'title': entry.title,
            'url': entry.link,
            'published': published_dt,
            'source': "Google News"
        })
    return articles

def fetch_nytimes():
    url = "https://rss.nytimes.com/services/xml/rss/nyt/Travel.xml"
    feed = feedparser.parse(url)
    articles = []

    for entry in feed.entries:
        published = entry.get("published_parsed") or entry.get("updated_parsed")
        published_dt = datetime(*published[:6], tzinfo=timezone.utc) if published else datetime.utcnow().replace(tzinfo=timezone.utc)
        articles.append({
            'title': entry.title,
            'url': entry.link,
            'published': published_dt,
            'source': "NYTimes"
        })
    return articles
