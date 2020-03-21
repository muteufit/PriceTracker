from requests import get
from bs4 import BeautifulSoup
from time import sleep
import smtplib
from email.message import EmailMessage

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36'}


def sendMail():
    msg = EmailMessage()
    # set your email address
    msg['From'] = 'Your Email Address'
    # set your friend email address
    msg['To'] = 'Your Client Email Address'
    # set subject
    msg['Subject'] = 'Seller'
    # set the body
    msg.set_content('you can now buy {0}'.format(url))
    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">Yay you can Buy It :) </h1>
            <a href={0}>product</a>
        </body>
    </html>
    """.format(url), subtype='html')
    # better methode than SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        # login with your email and password
        smtp.login('Your Email Address', 'Your Password')
        # send the message
        smtp.send_message(msg)


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


def checkPrice():
    domain = getDomain()
    if domain == 'jumia':
        return jumiaPrice()
    else:
        return souqPrice()


def checkBudget():
    # get user budget
    budget = int(input('Your Budget (Numbers) => '))
    if price < budget:
        print('========YES========')
        sendMail()
    else:
        print('================')
        print('You Need {0} LE to get this product'.format(price-budget))
        print('================')
        sleep(60)


# get product url
url = input('Product Url => ')
price = checkPrice()
checkBudget()
