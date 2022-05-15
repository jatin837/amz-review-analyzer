import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/HP-Pavilion-Graphics-35-56cms-14-dv0058TU/product-reviews/B08WB857GB/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

splash_url = 'http://localhost:8050/render.html'
res = requests.get(splash_url, params={
    'url':url,
    'wait':2
})

print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

reviews = soup.find_all('div', {
    'data-hook':'review'
})

for review in reviews:
    title = review.find('a', {
        'data-hook':'review-title'
    }).text.strip()

    rating = float(review.find('i', {
        'data-hook': 'review-star-rating'
    }).text.replace('out of 5 stars', '').strip())

    print(title, rating)