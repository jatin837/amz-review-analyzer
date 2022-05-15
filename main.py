from amz_reviews import Review
from lib import get_review_page_url, get_soup


def main():
    url = "https://www.amazon.in/HP-Pavilion-Graphics-35-56cms-14-dv0058TU/dp/B08WB857GB/ref=cm_cr_arp_d_product_top?ie=UTF8"

    splash_url = 'http://localhost:8050/render.html'

    soup = get_soup(url, splash_url)

    reviews = soup.find_all('div', {
        'data-hook':'review'
    })


    items = []
    for review in reviews:
        title = review.find('a', {
            'data-hook':'review-title'
        }).text.strip()

        rating = float(review.find('i', {
            'data-hook': 'review-star-rating'
        }).text.replace('out of 5 stars', '').strip())

        body = review.find('span', {
            'data-hook': 'review-body'
        }).text.strip()
        
        items.append(Review(title, rating, body))
    print(items)



if __name__ == "__main__":
    main()
