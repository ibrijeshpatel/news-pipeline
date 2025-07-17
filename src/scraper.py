import requests
from bs4 import BeautifulSoup
from utils import generate_id, parse_datetime

def fetch_skift():
    url = "https://skift.com/news/"
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        articles = []

        for item in soup.select("article"):
            link = item.find("a", href=True)
            title = item.find("h2")
            date = item.find("time")

            if link and title and date:
                articles.append({
                    "article_id": generate_id(link["href"]),
                    "url": link["href"],
                    "title": title.text.strip(),
                    "publication_ts": parse_datetime(date["datetime"]),
                    "source": "Skift"
                })
        return articles
    except Exception as e:
        print(f"[Skift] Error: {e}")
        return []

def fetch_phocuswire():
    url = "https://www.phocuswire.com/"
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        articles = []

        for item in soup.select("div.story-listing"):
            link = item.find("a", href=True)
            title = item.find("h3")
            date = item.find("div", class_="published-date")

            if link and title and date:
                full_url = "https://www.phocuswire.com" + link["href"]
                articles.append({
                    "article_id": generate_id(full_url),
                    "url": full_url,
                    "title": title.text.strip(),
                    "publication_ts": parse_datetime(date.text.strip()),
                    "source": "PhocusWire"
                })
        return articles
    except Exception as e:
        print(f"[PhocusWire] Error: {e}")
        return []
