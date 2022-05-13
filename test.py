from lib import *

url = "https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5XSG8Z/ref=cm_cr_arp_d_product_top?ie=UTF8&th=1"

def test_get_review_page_url():
    global url
    expected_url = "https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/product-reviews/B08N5XSG8Z/"
    res = get_review_page_url(url)
    assert res == expected_url

test_get_review_page_url()
