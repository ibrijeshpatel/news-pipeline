from scraper import fetch_skift, fetch_phocuswire
from db import connect_db, init_db, article_exists, insert_article
import os

def main():
    conn, cursor = connect_db()
    init_db(cursor)

    skift_articles = fetch_skift()
    phocus_articles = fetch_phocuswire()
    articles = skift_articles + phocus_articles

    new_count = 0
    for article in articles:
        if not article_exists(cursor, article["article_id"]):
            insert_article(cursor, article)
            new_count += 1

    conn.commit()

    # Get latest 5 articles
    cursor.execute("""
        SELECT title, url, publication_ts, source
        FROM articles
        ORDER BY publication_ts DESC
        LIMIT 5
    """)
    top_articles = cursor.fetchall()

    os.makedirs("output", exist_ok=True)
    with open("output/latest_articles.txt", "w", encoding="utf-8") as f:
        for title, url, ts, source in top_articles:
            line = f"{source} | {title} | {ts} | {url}"
            print(line)
            f.write(line + "\n")

    print(f"\n✅ Added {new_count} new articles.")
    conn.close()

if __name__ == "__main__":
    main()

