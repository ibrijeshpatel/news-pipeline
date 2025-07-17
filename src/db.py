import sqlite3

def connect_db(path="articles.db"):
    conn = sqlite3.connect(path)
    return conn, conn.cursor()

def init_db(cursor):
    with open("db/schema.sql") as f:
        cursor.executescript(f.read())

def article_exists(cursor, article_id):
    cursor.execute("SELECT 1 FROM articles WHERE article_id = ?", (article_id,))
    return cursor.fetchone() is not None

def insert_article(cursor, article):
    try:
        cursor.execute("""
            INSERT INTO articles (article_id, url, title, publication_ts, source)
            VALUES (?, ?, ?, ?, ?)
        """, (article["article_id"], article["url"], article["title"], article["publication_ts"], article["source"]))
    except sqlite3.IntegrityError:
        pass  # Already exists
