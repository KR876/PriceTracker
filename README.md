# PriceTracker

A Python tool that automatically collects grocery price data from three major Estonian retailers and stores it in a SQLite database for cross-store comparison and price history tracking.

## Features

- **Three-store support**: Rimi, Selver, Prisma
- **Large-scale collection**: ~50,000+ products (Selver ~19,000, Rimi ~17,000, Prisma in progress)
- **Price history**: each scraping run appends a timestamped price record, building a time series
- **Category mapping**: store categories mapped to a unified cross-store comparison structure
- **Modular design**: each store scraper is a separate module inheriting from a shared base class


## How Each Scraper Works

Each store exposes its data differently:

| Store | Method | Pagination |
|-------|--------|------------|
| Rimi | HTML scrape, `data-gtm-eec-product` JSON attributes | `?page=N` URL param |
| Selver | Elasticsearch REST API | `from`/`size` offset |
| Prisma | GraphQL POST requests | offset pagination |

## Usage

```bash
pip install requests beautifulsoup4

# Run all stores
python main.py

# Run a specific store
python main.py rimi
python main.py selver
python main.py prisma

# Run two stores at once
python main.py rimi selver
```

## Database Schema

```sql
CREATE TABLE products (
    id TEXT PRIMARY KEY,  -- store_categoryid_ean
    name TEXT,
    category TEXT,
    store TEXT
);

CREATE TABLE prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    price REAL,
    scraped_at TEXT
);
```

## Tech Stack

- Python 3.10+
- `requests`, `beautifulsoup4`
- SQLite (`sqlite3`)
