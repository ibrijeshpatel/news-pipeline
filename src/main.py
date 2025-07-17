from scraper import fetch_skift, fetch_phocuswire, fetch_google_news, fetch_nytimes
from db import init_db, save_article, get_latest_articles

if __name__ == "__main__":
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
        if save_article(article):
            new_count += 1

    # Display latest 5 articles
    latest = get_latest_articles(5)
    print("\n📰 Top 5 Latest Articles:\n")
    print("source | title | published | url")
    for source, title, published, url in latest:
        print(f"{source} | {title} | {published} | {url}")

    print(f"\n✅ Added {new_count} new articles.")
