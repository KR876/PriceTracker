import json
import urllib.parse
from scrapers.base_scraper import BaseScraper
from datetime import datetime

BASE_URL = 'https://www.selver.ee'
API_BASE = f'{BASE_URL}/api/catalog/vue_storefront_catalog_et'


class SelverScraper(BaseScraper):
    store_name = 'selver'

    def get_categories(self) -> list[tuple[str, str, str]]:
        """Fetch category tree and return all leaf categories."""
        url = f'{API_BASE}/category/_search'
        params = {
            'from': 0,
            'request': json.dumps({
                'query': {'bool': {'filter': {'term': {'url_key': 'tooted'}}}}
            }, separators=(',', ':'))
        }
        response = self.get(url, params=params)
        if response is None:
            return []

        data = response.json()
        hits = data.get('hits', {}).get('hits', [])
        if not hits:
            return []

        root = hits[0]['_source']
        categories = []
        self._walk(root.get('children_data', []), categories)
        return categories

    def _walk(self, nodes: list, result: list):
        for node in nodes:
            children = node.get('children_data', [])
            if children:
                self._walk(children, result)
            else:
                cat_id = str(node.get('id', ''))
                name = node.get('name', '')
                url_key = node.get('url_key', '')
                if cat_id and url_key:
                    result.append((name, url_key, cat_id))

    def build_url(self, slug: str, cat_id: str, page: int) -> tuple[str, dict]:
        request = {
            'query': {
                'bool': {
                    'filter': {
                        'bool': {
                            'must': [
                                {'terms': {'visibility': [2, 3, 4]}},
                                {'terms': {'status': [0, 1]}},
                                {'terms': {'category_ids': [int(cat_id)]}}
                            ]
                        }
                    }
                }
            },
            'sort': [{'category.position': {
                'order': 'asc', 'mode': 'min',
                'nested_path': 'category',
                'nested_filter': {'term': {'category.category_id': int(cat_id)}}
            }}]
        }
        params = {
            'from': (page - 1) * self.page_size,
            'size': self.page_size,
            'request': json.dumps(request, separators=(',', ':')),
            '_source_include': 'id,sku,name,final_price,product_main_ean'
        }
        return f'{API_BASE}/product/_search', params

    def parse_products(self, response) -> list[dict]:
        data = response.json()
        hits = data.get('hits', {}).get('hits', [])
        products = []
        for hit in hits:
            src = hit['_source']
            price = src.get('final_price') or src.get('price')
            if price and float(price) > 0:
                products.append({
                    'id': str(src.get('product_main_ean') or src.get('sku') or src.get('id')),
                    'name': src.get('name', ''),
                    'price': float(price),
                    'currency': 'EUR'
                })
        return products