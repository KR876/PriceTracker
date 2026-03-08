import json
import time

from bs4 import BeautifulSoup
from scrapers.base_scraper import BaseScraper
from datetime import datetime

BASE_URL = 'https://www.prismamarket.ee'
GRAPHQL_URL = 'https://graphql-api.prismamarket.ee/'
STORE_ID = '542860184'

class PrismaScraper(BaseScraper):
    store_name = 'prisma'

    def get_categories(self) -> list[tuple[str, str, str]]:
        """
        Fetch top-level categories from Prisma's /tooted page.
        Categories are embedded in __NEXT_DATA__ JSON in the HTML.
        Returns list of (name, slug, category_id).
        """
        response = self.get(f'{BASE_URL}/tooted')
        if response is None:
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        script = soup.find('script', id='__NEXT_DATA__')
        if not script:
            self.logger.error('Could not find __NEXT_DATA__ in Prisma HTML')
            return []

        data = json.loads(script.string)
        apollo = data['props']['pageProps']['apolloState']

        categories = []
        for key, val in apollo.items():
            if 'SectionCategoryNavigationItem' in key:
                cat_id = val.get('id', '')
                name = val.get('name', '')
                slug = val.get('slug', '')
                if cat_id and slug:
                    categories.append((name, slug, cat_id))

        return categories

    def _fetch_products_page(self, slug: str, offset: int, limit: int = None):
        if limit is None:
            limit = self.page_size
        variables = {
            'facets': [{'key': 'brandName', 'order': 'asc'}, {'key': 'labels'}],
            'fetchSponsoredContent': True,
            'includeAgeLimitedByAlcohol': True,
            'limit': limit,
            'offset': offset,
            'queryString': '',
            'slug': slug,
            'storeId': STORE_ID,
            'useRandomId': True
        }
        params = {
            'operationName': 'RemoteFilteredProducts',
            'variables': json.dumps(variables, separators=(',', ':')),
            'extensions': json.dumps({
                'persistedQuery': {
                    'version': 1,
                    'sha256Hash': '883303cea3d924219a577b2df9583bd528531b3f4e2c3adcb7110811f2906a2b'
                }
            }, separators=(',', ':'))
        }
        try:
            response = self.session.get(
                GRAPHQL_URL,
                params=params,
                timeout=self.timeout,
                headers={
                    'Origin': 'https://www.prismamarket.ee',
                    'Referer': 'https://www.prismamarket.ee/tooted',
                    'x-client-name': 'skaupat-web',
                    'x-client-version': 'production-a97f2f06397bbd3a5881b61681a5abf012a032a7',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0',
                    'Accept-Language': 'et',
                }
            )
            response.raise_for_status()
            time.sleep(self.delay)
            return response
        except Exception as e:
            self.logger.error(f'GraphQL request failed: {e}')
            return None

    def parse_products(self, response) -> list[dict]:
        data = response.json()
        items = data.get('data', {}).get('store', {}).get('products', {}).get('items', [])
        products = []
        for item in items:
            price = item.get('price')
            if price is not None and float(price) > 0:
                products.append({
                    'id':       str(item.get('id', item.get('ean', ''))),
                    'name':     item.get('name', ''),
                    'price':    float(price),
                    'currency': 'EUR'
                })
        return products

    def scrape_category(self, name: str, slug: str, cat_id: str) -> int:

        offset = 0
        total = 0
        scraped_at = datetime.now().isoformat()
        total_available = None  # will be set from first response

        while True:
            # don't request more than what's left
            remaining = total_available - offset if total_available is not None else self.page_size
            limit = min(self.page_size, remaining) if remaining > 0 else self.page_size

            response = self._fetch_products_page(slug, offset, limit)

            data = response.json()
            products_data = data.get('data', {}).get('store', {}).get('products', {})

            # get total on first page
            if total_available is None:
                total_available = products_data.get('total', 0)
                self.logger.info(f'  {name} | total available: {total_available}')

            products = self.parse_products(response)
            if not products:
                break

            for p in products:
                self.db.save_product_and_price(
                    product_id=p['id'],
                    name=p['name'],
                    category=cat_id,
                    price=p['price'],
                    scraped_at=scraped_at,
                    currency=p['currency']
                )
                total += 1

            self.logger.info(f'  {name} | offset {offset} | {len(products)} products')
            offset += self.page_size

            if offset >= total_available:
                break

        return total