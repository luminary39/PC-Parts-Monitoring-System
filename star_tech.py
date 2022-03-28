import requests
from bs4 import BeautifulSoup


def star_tech_price_check(url):
    try:

        sorce_code = requests.get(url=url)

        code = BeautifulSoup(sorce_code.content, 'html.parser')

        # print(code.prettify())

        product = code.find(id="product")

        main_price = product.find_all('tr')[0].find_all('td')[1].string
        price = main_price.replace(",", "").replace("৳", "")
        return int(price)

    except:

        return "To Be Announced!"

