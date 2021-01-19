from modules.souq import Souq
from modules.jumia import Jumia


class WebsiteController:

    def __init__(self, url):
        self.url = url

    def getDomain(self, url):
        domain = url.split('.')[1].split('.')[0]
        return domain

    def checkAbility(self, domain):
        if domain == 'souq' or domain == 'jumia':
            pass
        else:
            raise Exception('ERROR : Souq Or Jumia Only')

    def getPrice(self):
        domain = self.getDomain(self.url)
        self.checkAbility(domain)
        if domain == 'jumia':
            jumia = Jumia(self.url)
            return jumia.price()
            # Todo: send to jumia class
        else:
            souq = Souq(self.url)
            return souq.price()
