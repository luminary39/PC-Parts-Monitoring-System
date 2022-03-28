import requests
from bs4 import BeautifulSoup


def ryans_price_check(url):

    try:
        doc = requests.get(url)
        code = BeautifulSoup(doc.content, 'html.parser')

        special_prise = code.find_all(text="Special Price ")

        price = special_prise[0].parent.find('span').contents[0]

        price = price.replace(' ', '').replace(',', '')


        return int(price)

    except:

        return "Out Of Stock"
