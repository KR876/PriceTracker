import json
import logging
from database.db_manager import DatabaseManager
from scrapers.Prisma import PrismaScraper
from scrapers.rimi import RimiScraper

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(name)s] %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)


def load_config(path='config.json') -> dict:
    with open(path, 'r') as f:
        return json.load(f)


def run():
    config = load_config()
    db = DatabaseManager()

    scraper = PrismaScraper(config, db)
    scraper.run()

    stats = db.get_stats()
    logging.info(f'Database: {stats["products"]} products, {stats["price_records"]} price records')
    logging.info(f'First scraped: {stats["first_scraped"]}')
    logging.info(f'Last scraped:  {stats["last_scraped"]}')


if __name__ == '__main__':
    run()