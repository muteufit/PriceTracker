from requests import get
from bs4 import BeautifulSoup


class Souq:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36'}

    def __init__(self, url):
        self.url = url

    def price(self):
        # make request
        response = get(self.url, headers=self.headers)
        # init parses
        soup = BeautifulSoup(response.text, 'html.parser')
        # make instance
        instan = soup.find(class_='price is sk-clr1').get_text(strip=True)
        return float(instan.replace('EGP', '').replace(',', ''))
