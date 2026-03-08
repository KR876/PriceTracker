import requests
import logging
import time
from abc import ABC, abstractmethod
from datetime import datetime
from database.db_manager import DatabaseManager


class BaseScraper(ABC):
    """
    Base class for store scrapers.
    Subclasses implement get_categories(), build_url(), and parse_products().
    """

    store_name = None

    def __init__(self, config: dict, db: DatabaseManager):
        self.config = config
        self.db = db
        self.delay = config.get('delay', 1.0)
        self.page_size = config.get('page_size', 100)
        self.timeout = config.get('timeout', 10)
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': config.get('user_agent', 'PriceTracker/1.0')})
        self.logger = logging.getLogger(self.store_name or self.__class__.__name__)

    def get(self, url, **kwargs):
        """GET request with error handling and rate limiting."""
        try:
            response = self.session.get(url, timeout=self.timeout, **kwargs)
            response.raise_for_status()
            time.sleep(self.delay)
            return response
        except requests.RequestException as e:
            self.logger.error(f'Request failed: {url} — {e}')
            return None

    @abstractmethod
    def get_categories(self) -> list[tuple[str, str, str]]:
        """Return list of (name, slug, category_id) for all leaf categories."""
        pass

    @abstractmethod
    def build_url(self, slug: str, cat_id: str, page: int) -> tuple[str, dict]:
        """Return (url, params) for a given category page."""
        pass

    @abstractmethod
    def parse_products(self, response) -> list[dict]:
        """
        Parse response and return list of product dicts.
        Each dict must have: id, name, price, currency.
        """
        pass

    def scrape_category(self, name: str, slug: str, cat_id: str) -> int:
        """Scrape all pages of a category. Returns number of records saved."""
        page = 1
        total = 0
        scraped_at = datetime.now().isoformat()

        while True:
            url, params = self.build_url(slug, cat_id, page)
            response = self.get(url, params=params)

            if response is None:
                break

            products = self.parse_products(response)

            if not products:
                break

            for p in products:
                if p.get('price') is not None:
                    self.db.save_product_and_price(
                        product_id=str(p['id']),
                        name=p.get('name', ''),
                        category=cat_id,
                        price=p['price'],
                        scraped_at=scraped_at,
                        currency=p.get('currency', 'EUR')
                    )
                    total += 1

            self.logger.info(f'  {name} | page {page} | {len(products)} products')
            page += 1

        return total

    def run(self) -> int:
        """Run the full scrape. Returns total records saved."""
        self.logger.info(f'Starting {self.store_name} scraper')
        categories = self.get_categories()
        self.logger.info(f'Found {len(categories)} categories')

        total = 0
        for i, (name, slug, cat_id) in enumerate(categories, 1):
            self.logger.info(f'[{i}/{len(categories)}] {name}')
            total += self.scrape_category(name, slug, cat_id)

        self.logger.info(f'{self.store_name} done — {total} total records saved')
        return total