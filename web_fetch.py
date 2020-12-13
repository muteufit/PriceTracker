from requests import get
from bs4 import BeautifulSoup
from price_tracker import url

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36'}


def getDomain():
    domain = url.split('.')[1].split('.')[0]
    return domain


def makeRequest():
    # make request
    response = get(url, headers=headers)
    # init parses
    soup = BeautifulSoup(response.text, 'html.parser')
    # get the right className
    className = checkClass()
    # make instance
    instan = soup.find(class_=className).get_text()
    # loop throw the result to get price
    e = ''
    for i in instan:
        try:
            int(i)
            e += i
        except:
            pass
    return e


def checkClass():
    domainName = getDomain()
    if domainName == 'jumia':
        return '-b -ltr -tal -fs24'
    elif domainName == 'souq':
        return 'price is sk-clr1'
    else:
        print('ERROR : Souq Or Jumia Only')
        exit()


def jumiaPrice():
    price = makeRequest()
    return float(price)


def souqPrice():
    price = makeRequest()[:-2]
    return float(price)
