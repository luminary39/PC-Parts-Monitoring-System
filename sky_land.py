import requests
from bs4 import BeautifulSoup


def sky_land_price_checker(url):

    try:

        sorce_code = requests.get(url)

        code = BeautifulSoup(sorce_code.content, 'html.parser')

        product = code.find_all("bdi")[18]

        price = product.text

        price = int(price.replace("৳","").replace(",", ""))

        if "Out Of Stock" in sorce_code.text:
            result = "Out Of Stock!"

            return result
        return price


    except:
        return "Something went wrong!"



