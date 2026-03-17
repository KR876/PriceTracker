# PriceTracker

Scrapes grocery prices from Rimi, Selver and Prisma into a local SQLite database. Supports cross-store price comparison and builds a price history over time with repeated runs.


## Features

- **Three-store support**: Rimi, Selver, Prisma (~60,000 products total)
- **Price history**: each scraping run appends timestamped price records, building a time series
- **Cross-store analysis**: unified category mapping across all three stores

## How Each Scraper Works

| Store | Method | Pagination |
|-------|--------|------------|
| Rimi | HTML scrape via `data-gtm-eec-product` attributes | `?page=N` URL param |
| Selver | Elasticsearch REST API | `from`/`size` offset |
| Prisma | GraphQL persisted queries | `from` offset |

## Usage
```bash
pip install requests beautifulsoup4 pandas rapidfuzz

python main.py             # Run all stores
python main.py rimi selver # Run specific stores
python analysis.py         # Cross-store analasysis
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

Re-running the scraper appends new price records without touching old ones, so you get a price time series automatically.

## Tech Stack

- Python 3.10+
- `requests`, `beautifulsoup4`, `pandas`, `rapidfuzz`
- SQLite (`sqlite3`)