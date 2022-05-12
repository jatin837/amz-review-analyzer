from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.amazon.in/HP-Pavilion-Graphics-35-56cms-14-dv0058TU/product-reviews/B08WB857GB/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews")


cont = res.text

soup = BeautifulSoup(cont, 'html.parser')

soup.prettify()

with open('out.html', 'w') as f:
    f.write(cont)
