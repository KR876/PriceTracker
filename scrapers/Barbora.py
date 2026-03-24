import re
import json
import time
from scrapers.base_scraper import BaseScraper

BASE_URL = 'https://barbora.ee'

TOP_LEVEL_SLUGS = [
    'koogiviljad-puuviljad',
    'leivad-saiad-kondiitritooted',
    'liha-kala-valmistoit',
    'kauasailivad-toidukaubad',
    'kulmutatud-tooted',
    'joogid',
    'enesehooldustooted',
    'puhastustarbed-ja-lemmikloomatooted',
    'lastekaubad',
    'kodukaubad-ja-vaba-aeg',
    'piimatooted-ja-munad',
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'et,en;q=0.9',
    'Referer': 'https://barbora.ee/',
}


class BarboraScraper(BaseScraper):
    store_name = 'barbora'

    def build_url(self, slug, cat_id, page):
        return f'{BASE_URL}/{slug}', ({'page': page} if page > 1 else {})

    def parse_products(self, response):
        m = re.search(r'window\.b_productList\s*=\s*(\[.*?\]);', response.text, re.DOTALL)
        if not m:
            return []
        try:
            items = json.loads(m.group(1))
        except json.JSONDecodeError:
            return []
        return [
            {'id': str(p['id']), 'name': p['title'], 'price': float(p['price']), 'currency': 'EUR'}
            for p in items if p.get('price') and float(p['price']) > 0 and p.get('id') and p.get('title')
        ]

    def _collect_leaf_slugs(self, top_slug):
        """Paginate through a top-level slug and collect unique leaf slugs from category_path_url."""
        slugs = set()
        resp = self.get(f'{BASE_URL}/{top_slug}', headers=HEADERS)
        if resp is None:
            return slugs
        m = re.search(r'window\.b_productList\s*=\s*(\[.*?\]);', resp.text, re.DOTALL)
        if not m:
            return slugs
        for p in json.loads(m.group(1)):
            path = p.get('category_path_url', '')
            name = p.get('category_name_full_path', path).split('/')[-1].strip()
            if path:
                slugs.add((name, path))
        return slugs

    def get_categories(self):
        self.logger.info('Collecting Barbora leaf category slugs...')
        categories = set()
        for top_slug in TOP_LEVEL_SLUGS:
            leaves = self._collect_leaf_slugs(top_slug)
            categories.update(leaves)
            self.logger.info(f'{top_slug}: {len(leaves)} leaf categories found')
            time.sleep(self.config.get('delay', 1.0))
        result = [(name, slug, slug) for name, slug in sorted(categories)]
        self.logger.info(f'Total: {len(result)} Barbora categories')
        return result

    def scrape_category(self, name, slug, cat_id):
        from datetime import datetime
        page = 1
        total = 0
        scraped_at = datetime.now().isoformat()
        while True:
            resp = self.get(f'{BASE_URL}/{slug}', headers=HEADERS, params={'page': page} if page > 1 else {})
            if resp is None:
                break
            products = self.parse_products(resp)
            if not products:
                break
            for p in products:
                self.db.save_product_and_price(
                    product_id=p['id'], name=p['name'], category=slug,
                    price=p['price'], scraped_at=scraped_at, store='barbora'
                )
                total += 1
            self.logger.info(f'  {name} | page {page} | {len(products)} products')
            page += 1
            time.sleep(self.config.get('delay', 1.0))
        return total