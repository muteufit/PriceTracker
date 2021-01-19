from requests import get
from bs4 import BeautifulSoup
from json import loads


class Jumia:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36'}

    def __init__(self, url):
        self.url = url

    def price(self):
        res = get(self.url, headers=self.headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        scripts = soup.find_all('script')
        script = scripts[2].contents
        jsonPrice = loads(''.join(script))
        return float(jsonPrice['mainEntity']['offers']['price'])
