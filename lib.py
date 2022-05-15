from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

def get_review_page_url(url:str) -> str:
    parse_res = urlparse(url)
    scheme = parse_res.scheme
    netloc = parse_res.netloc
    product = parse_res.path[1:].split('/')[0]
    ASIN = parse_res.path[1:].split('/')[2]
    new_url = f"{scheme}://{netloc}/{product}/product-reviews/{ASIN}/"
    return new_url

def get_soup(url: str, splash_url: str):
    url = get_review_page_url(url)
    res = requests.get(splash_url, params = {
        "url": url,
        "wait": 2
    })
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

