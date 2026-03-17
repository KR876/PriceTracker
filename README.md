# PriceTracker

A Python tool that automatically collects grocery price data from three major Estonian retailers and stores it in a SQLite database for cross-store comparison and price history tracking.

## Features

- **Three-store support**: Rimi, Selver, Prisma (~50,000 products total)
- **Price history**: each scraping run appends timestamped price records, building a time series
- **Cross-store analysis**: unified category mapping across all three stores
- **Modular design**: each store scraper inherits from a shared base class

## How Each Scraper Works

| Store | Method | Pagination |
|-------|--------|------------|
| Rimi | HTML scrape via `data-gtm-eec-product` attributes | `?page=N` URL param |
| Selver | Elasticsearch REST API | `from`/`size` offset |
| Prisma | GraphQL persisted queries | `from` offset |

## Usage
```bash
pip install requests beautifulsoup4 pandas rapidfuzz

# Run all stores
python main.py

# Run specific stores
python main.py rimi
python main.py rimi selver

# Cross-store price analysis
python analysis.py
```

## Database Schema
```sql
CREATE TABLE products (
    id TEXT PRIMARY KEY,  -- format: store_categoryid_ean
    name TEXT,
    category TEXT,
    store TEXT
);

CREATE TABLE prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    price REAL,
    scraped_at TEXT        -- ISO timestamp, enables price history
);

CREATE TABLE categories (
    id TEXT,
    store TEXT,
    name TEXT,
    PRIMARY KEY (id, store)
);
```

## Price History

Re-running the scraper on a different day automatically adds new price records without overwriting old ones. Over time this builds a genuine price time series per product.

## Tech Stack

- Python 3.10+
- `requests`, `beautifulsoup4`, `pandas`, `rapidfuzz`
- SQLite (`sqlite3`)