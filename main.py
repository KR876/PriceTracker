import json
import logging
import sys
from database.db_manager import DatabaseManager
from scrapers.Prisma import PrismaScraper
from scrapers.rimi import RimiScraper
from scrapers.Selver import SelverScraper

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

    scrapers = []

    if len(sys.argv) > 1:
        names = sys.argv[1:]
        scraper_map = {
            'rimi': RimiScraper,
            'prisma': PrismaScraper,
            'selver': SelverScraper,
        }
        for name in names:
            if name in scraper_map:
                scrapers.append(scraper_map[name](config, db))
            else:
                logging.warning(f'Unknown scraper: {name}')
    else:
        scrapers = [RimiScraper(config, db), PrismaScraper(config, db)]

    for scraper in scrapers:
        scraper.run()

    stats = db.get_stats()
    logging.info(f'Database: {stats["products"]} products, {stats["price_records"]} price records')
    logging.info(f'First scraped: {stats["first_scraped"]}')
    logging.info(f'Last scraped:  {stats["last_scraped"]}')


if __name__ == '__main__':
    run()