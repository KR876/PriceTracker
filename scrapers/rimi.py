import json
from bs4 import BeautifulSoup
from scrapers.base_scraper import BaseScraper

BASE_URL = 'https://www.rimi.ee'


class RimiScraper(BaseScraper):
    store_name = 'rimi'

    def get_categories(self) -> list[tuple[str, str, str]]:
        """Fetch category tree from Rimi's API and return all leaf categories."""
        url = f'{BASE_URL}/epood/api/v1/content/category-tree?locale=ee'
        response = self.get(url)
        if response is None:
            return []

        data = response.json()
        top_level = data.get('categories', data) if isinstance(data, dict) else data

        categories = []
        self._walk(top_level, categories)
        return categories

    def _walk(self, nodes: list, result: list):
        """Recursively walk the category tree to collect leaf categories."""
        for node in nodes:
            descendants = node.get('descendants') or []
            url_path = node.get('url', '')

            if descendants:
                self._walk(descendants, result)
            else:
                # Leaf node — extract slug and ID from URL
                # URL format: /epood/ee/tooted/{slug}/c/{cat_id}
                parts = url_path.split('/c/')
                if len(parts) == 2:
                    cat_id = parts[1]
                    slug = parts[0].split('/tooted/')[-1]
                    result.append((node.get('name', ''), slug, cat_id))
                    self.db.save_category(cat_id, 'rimi', node.get('name', ''))

    def build_url(self, slug: str, cat_id: str, page: int) -> tuple[str, dict]:
        url = f'{BASE_URL}/epood/ee/tooted/{slug}/c/{cat_id}'
        params = {
            'currentPage': page,
            'pageSize': self.page_size,
            'query': f':relevance:allCategories:{cat_id}:assortmentStatus:inAssortment'
        }
        return url, params

    def parse_products(self, response) -> list[dict]:
        """Parse product data from data-gtm-eec-product attributes in the HTML."""
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all(attrs={'data-gtm-eec-product': True})

        products = []
        for card in cards:
            try:
                data = json.loads(card['data-gtm-eec-product'])
                products.append({
                    'id':       data['id'],
                    'name':     data.get('name', ''),
                    'price':    data.get('price'),
                    'currency': data.get('currency', 'EUR')
                })
            except (json.JSONDecodeError, KeyError):
                continue

        return products