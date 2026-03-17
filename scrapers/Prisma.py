import json
import time
import uuid
import urllib.parse
import requests
from datetime import datetime
from scrapers.base_scraper import BaseScraper

# Top-level category slugs from prismamarket.ee/tooted
TOP_LEVEL_SLUGS = [
    'puu-ja-koogiviljad',
    'leivad-kupsised-ja-kupsetised',
    'liha-ja-taimsed-valgud',
    'kala-ja-mereannid',
    'piim-munad-ja-rasvad',
    'juustud',
    'valmistoit',
    'olid-vurtsid-maitseained',
    'kuivtooted-ja-kupsetamine',
    'joogid',
    'kulmutatud-toidud',
    'maiustused-ja-suupisted',
    'kosmeetika-ja-hugieen',
    'loodustooted-ja-toidulisandid',
    'kodu-ja-majapidamistarbed',
    'lapsed',
    'lemmikloomad',
    'kodu-ja-vaba-aeg',
    'sport',
    'kodumasinad-ja-elektroonika'
]

class PrismaScraper(BaseScraper):
    store_name = 'prisma'
    BASE_URL = 'https://graphql-api.prismamarket.ee/'
    HASH = '883303cea3d924219a577b2df9583bd528531b3f4e2c3adcb7110811f2906a2b'
    STORE_ID = '542860184'
    LIMIT = 24
    HEADERS = {
        'Origin': 'https://www.prismamarket.ee',
        'Referer': 'https://www.prismamarket.ee/',
        'x-client-name': 'skaupat-web',
        'x-client-version': 'production-f6891b48cf27f0685872d6bcec3ef5c295f3f41a',
        'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0',
        'Accept': '*/*',
        'Accept-Language': 'et',
    }

    def build_url(self, category, page):
        """Not used - Prisma uses _fetch() directly."""
        return None

    def parse_products(self, data):
        """Not used - Prisma parses products directly in scrape_category()."""
        return []

    def _fetch(self, slug, offset=0):
        """Fetch a page of products for a given slug and offset."""
        variables = {
            'facets': [{'key': 'brandName', 'order': 'asc'}, {'key': 'labels'}],
            'generatedSessionId': str(uuid.uuid4()),
            'fetchSponsoredContent': False,
            'includeAgeLimitedByAlcohol': True,
            'limit': self.LIMIT,
            'from': offset,
            'queryString': '',
            'slug': slug,
            'storeId': self.STORE_ID,
            'useRandomId': False,
        }
        extensions = {
            'persistedQuery': {'version': 1, 'sha256Hash': self.HASH}
        }
        url = (
            f"{self.BASE_URL}?operationName=RemoteFilteredProducts"
            f"&variables={urllib.parse.quote(json.dumps(variables))}"
            f"&extensions={urllib.parse.quote(json.dumps(extensions))}"
        )
        resp = requests.get(url, headers=self.HEADERS,
                            timeout=self.config.get('timeout', 10))
        return resp.json()

    def _collect_subcategory_slugs(self, top_slug):
        """
        Paginate through all pages of a top-level category and collect
        all 2-level subcategory slugs from hierarchyPath.
        """
        slugs = set()
        offset = 0

        while True:
            try:
                data = self._fetch(top_slug, offset=offset)
                products_data = data.get('data', {}).get('store', {}).get('products', {})
                items = products_data.get('items', [])
                total = products_data.get('total', 0)

                if not items:
                    break

                for item in items:
                    for path in item.get('hierarchyPath', []):
                        item_slug = path.get('slug', '')
                        if len(item_slug.split('/')) == 2:
                            slugs.add((path.get('name', item_slug), item_slug))

                offset += self.LIMIT
                if offset >= total:
                    break

                time.sleep(0.5)

            except Exception as e:
                self.logger.warning(f"Slug collection failed for {top_slug} at offset {offset}: {e}")
                break

        return slugs

    def get_categories(self):
        """
        Build the full category list by collecting subcategory slugs
        from the first page of each top-level category.
        """
        self.logger.info('Collecting Prisma subcategory slugs...')
        categories = set()
        for top_slug in TOP_LEVEL_SLUGS:
            subcats = self._collect_subcategory_slugs(top_slug)
            if subcats:
                categories.update(subcats)
                self.logger.info(f'{top_slug}: found {len(subcats)} subcategories')
            else:
                # Fall back to top-level slug if no subcategories found
                categories.add((top_slug, top_slug))
            time.sleep(self.config.get('delay', 1.0))
        return [(name, slug, slug) for name, slug in sorted(categories)]

    def scrape_category(self, name, slug, cat_id):
        """Paginate through all products in a category using offset."""
        offset = 0
        total = 0
        scraped_at = datetime.now().isoformat()

        while True:
            try:
                data = self._fetch(slug, offset)
                products_data = (data.get('data', {}).get('store', {})
                                     .get('products', {}))
                items = products_data.get('items', [])

                if not items:
                    break

                for p in items:
                    ean = p.get('ean') or p.get('id')
                    pricing = p.get('pricing', {})
                    price = pricing.get('currentPrice') or p.get('price')
                    pname = p.get('name')
                    if ean and price and pname:
                        self.db.save_product_and_price(
                            product_id=str(ean),
                            name=pname,
                            category=slug,
                            price=float(price),
                            scraped_at=scraped_at,
                            store='prisma'
                        )
                        total += 1

                total_available = products_data.get('total', 0)
                offset += self.LIMIT
                if offset >= total_available:
                    break

                time.sleep(self.config.get('delay', 1.0))

            except Exception as e:
                self.logger.error(f"Error scraping {slug} at offset {offset}: {e}")
                break

        return total