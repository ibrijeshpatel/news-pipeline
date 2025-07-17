# News Pipeline: Skift, PhocusWire, Google News & NYTimes Scraper

A Python-powered data pipeline that fetches the latest travel and general news articles from Skift, PhocusWire, Google News, and The New York Times, stores them in a SQLite database, and displays the 5 most recent entries in the terminal and saves them to a text file.

## Features

- Multi-source scraping: Skift, Google News, NYTimes (RSS-based), PhocusWire attempted
- Incremental loading: Avoids duplicate articles using a hash-based system
- SQLite storage: Lightweight and local database for persistence
- Modular structure: Clean, maintainable code in separate modules
- Output: Displays and writes the 5 latest articles to `output/latest_articles.txt`
- Error handling: Graceful failure for unsupported or broken feeds

## PhocusWire Status

This project attempts to fetch articles from PhocusWire, but no articles are currently returned. Possible reasons include:

- The RSS feed structure may have changed
- The site may block automated scraping
- The feed URL could be deprecated or inaccessible

The script includes logging to indicate if no articles are fetched from PhocusWire or any other source.


Project Structure

news-pipeline/
├── src/
│   ├── main.py              # Main script to run the pipeline
│   ├── scraper.py           # Contains scraping functions per source
│   └── db.py                # DB initialization and insert/query helpers
│
├── output/
│   └── latest_articles.txt  # Text file with latest 5 articles
│
├── news.db                  # SQLite database file
├── requirements.txt         # List of Python dependencies
└── README.md                # Project documentation




## Getting Started

## 🚀 Getting Started

# Step 1: Clone the repository
git clone https://github.com/your-username/news-pipeline.git
cd news-pipeline

# Step 2: (Recommended) Create and activate a virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Step 3: Install project dependencies
pip install -r requirements.txt

# Step 4: Run the news pipeline script
python src/main.py




## After running the script:

A news.db SQLite file will be created (if not present)
New articles will be added (duplicates skipped)
The 5 latest articles will be printed in the terminal
A text file output/latest_articles.txt will be updated with the same 5 articles