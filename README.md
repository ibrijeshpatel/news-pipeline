# News Pipeline: Skift & PhocusWire Scraper

A Python-powered data pipeline that fetches the latest travel industry articles from Skift and PhocusWire, 
stores them in a SQLite database, and shows the 5 most recent news entries.

## Features
- Web scraping via BeautifulSoup
- Incremental loading using hashed article IDs
- SQLite for lightweight persistence
- Error handling & logging
- Modular codebase for clarity
- Output saved to `output/latest_articles.txt`

## Tech Stack
- Python
- BeautifulSoup
- Requests
- SQLite
- SQL

## Quickstart
```bash
git clone https://github.com/your-username/news-pipeline.git
cd news-pipeline
pip install -r requirements.txt
python src/main.py

