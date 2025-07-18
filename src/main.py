import os
from scraper import fetch_skift, fetch_phocuswire, fetch_google_news, fetch_nytimes
from db import init_db, save_article, get_latest_articles

OUTPUT_DIR = "output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "latest_articles.txt")

def save_latest_to_file(articles):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for source, title, published, url in articles:
            f.write(f"Source: {source}\n")
            f.write(f"Title: {title}\n")
            f.write(f"Published: {published}\n")
            f.write(f"URL: {url}\n")
            f.write("\n" + "-"*40 + "\n\n")

def main():
    init_db()

    all_articles = []

    # Skift
    skift_articles = fetch_skift()
    print(f"🔍 Skift fetched: {len(skift_articles)} articles")
    all_articles.extend(skift_articles)

    # PhocusWire
    phocuswire_articles = fetch_phocuswire()
    if phocuswire_articles:
        print(f"🔍 PhocusWire fetched: {len(phocuswire_articles)} articles")
        all_articles.extend(phocuswire_articles)
    else:
        print("⚠️  PhocusWire returned no articles. Possible reasons: RSS feed not supported, structure changed, or feed temporarily unavailable.")

    # Google News
    google_articles = fetch_google_news()
    print(f"🔍 Google News fetched: {len(google_articles)} articles")
    all_articles.extend(google_articles)

    # NYTimes
    nytimes_articles = fetch_nytimes()
    print(f"🔍 NYTimes fetched: {len(nytimes_articles)} articles")
    all_articles.extend(nytimes_articles)

    # Save unique articles
    new_count = 0
    for article in all_articles:
        # Convert published datetime to ISO string if needed
        if hasattr(article['published'], 'isoformat'):
            article['published'] = article['published'].isoformat()
        if save_article(article):
            new_count += 1

    # Display latest 5 articles
    latest = get_latest_articles(5)
    print("\n📰 Top 5 Latest Articles:\n")
    print("source | title | published | url")
    print("-" * 80)
    for source, title, published, url in latest:
        print(f"{source} | {title} | {published} | {url}")

    # Save to output file
    save_latest_to_file(latest)
    print(f"\n✅ Added {new_count} new articles.")
    print(f"✅ Latest articles saved to '{OUTPUT_FILE}'")

if __name__ == "__main__":
    main()
