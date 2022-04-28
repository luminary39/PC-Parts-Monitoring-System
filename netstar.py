import requests
from bs4 import BeautifulSoup


def netstar_price_check(url):
    try:
        request = requests.get(url)

        code = BeautifulSoup(request.content, 'html.parser')

        price = int(float(
            code.find_all("div", class_="entry-summary")[0].find_all("span")[0].text.replace("৳", "").strip().replace(
                ",", "")))

        if "Out of stock" in request.text:
            return "Not Available Currently!"

        return price


    except:
        pass



