import requests
from bs4 import BeautifulSoup


def netstar_price_checker(url):
    try:
        request = requests.get(url)

        code = BeautifulSoup(request.content, 'html.parser')

        price = int(float(
            code.find_all("div", class_="entry-summary")[0].find_all("span")[0].text.replace("৳", "").strip().replace(
                ",", "")))

        if "Out of stock" in request.text:
            return "Out Of Stock!"

        return price


    except:
        pass


netstar_price_checker("https://www.netstar.com.bd/product/gigabyte-aorus-geforce-rtx-2080-ti-graphics-card/")
