CREATE TABLE IF NOT EXISTS articles (
    article_id TEXT PRIMARY KEY,
    url TEXT NOT NULL,
    title TEXT NOT NULL,
    publication_ts TEXT NOT NULL,
    source TEXT NOT NULL
);

