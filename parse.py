import requests
from bs4 import BeautifulSoup

def get_amazon_search(search_query):
    url = f"https://www.amazon.in/s?k={search_query}"
    print(url)
    page=requests.get(url, cookies=cookie, headers=header)
    if page.status_code == 200:
        return page
    else:
        return "error"

data_asin=[]
res = get_amazon_search('tital+men+watches')
soup=BeautifulSoup(res.content)
