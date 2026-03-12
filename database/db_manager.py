import sqlite3
from pathlib import Path


class DatabaseManager:
    def __init__(self, db_path='prices.db'):
        self.db_path = db_path
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        with self._connect() as conn:
            conn.executescript('''
                CREATE TABLE IF NOT EXISTS products (
                    id       TEXT PRIMARY KEY,
                    name     TEXT,
                    category TEXT,
                    store    TEXT
                );

                CREATE TABLE IF NOT EXISTS prices (
                    id         INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id TEXT NOT NULL,
                    price      REAL NOT NULL,
                    currency   TEXT DEFAULT "EUR",
                    scraped_at TEXT NOT NULL,
                    FOREIGN KEY (product_id) REFERENCES products(id)
                );

                CREATE INDEX IF NOT EXISTS idx_prices_product ON prices(product_id);
                CREATE INDEX IF NOT EXISTS idx_prices_time    ON prices(scraped_at);
                CREATE UNIQUE INDEX IF NOT EXISTS idx_prices_unique ON prices(product_id, scraped_at);
            ''')

    def save_product_and_price(self, product_id, name, category, price, scraped_at, currency='EUR', store=None):
        composite_id = f"{store}_{category}_{product_id}"
        with self._connect() as conn:
            cursor = conn.execute('''
                                  INSERT OR IGNORE INTO products (id, name, category, store)
                                  VALUES (?, ?, ?, ?)
                                  ''', (composite_id, name, category, store))
            print(f"products rowcount: {cursor.rowcount}, id: {composite_id}")
            conn.execute('''
                         INSERT OR IGNORE INTO prices (product_id, price, currency, scraped_at)
                         VALUES (?, ?, ?, ?)
                         ''', (composite_id, price, currency, scraped_at))

    def get_stats(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM products')
            products = cursor.fetchone()[0]
            cursor.execute('SELECT COUNT(*) FROM prices')
            prices = cursor.fetchone()[0]
            cursor.execute('SELECT MIN(scraped_at), MAX(scraped_at) FROM prices')
            date_range = cursor.fetchone()
            return {
                'products': products,
                'price_records': prices,
                'first_scraped': date_range[0],
                'last_scraped': date_range[1]
            }