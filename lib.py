from urllib.parse import urlparse

def get_review_page_url(url:str) -> str:
    parse_res = urlparse(url)
    scheme = parse_res.scheme
    netloc = parse_res.netloc
    product = parse_res.path[1:].split('/')[0]
    ASIN = parse_res.path[1:].split('/')[2]
    new_url = f"{scheme}://{netloc}/{product}/product-reviews/{ASIN}/"
    return new_url
