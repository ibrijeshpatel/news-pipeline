import sqlite3

DB_PATH = "news.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT UNIQUE,
            published TIMESTAMP,
            source TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_article(article):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO articles (title, url, published, source)
            VALUES (?, ?, ?, ?)
        """, (article['title'], article['url'], article['published'], article['source']))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # Duplicate URL (already saved)
        return False
    finally:
        conn.close()

def get_latest_articles(limit=5):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT source, title, published, url
        FROM articles
        ORDER BY published DESC
        LIMIT ?
    """, (limit,))
    rows = cur.fetchall()
    conn.close()
    return rows  # ✅ returns list of tuples
