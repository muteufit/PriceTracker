from web_fetch import getDomain, jumiaPrice, souqPrice
from time import sleep
from send_mail import sendMail

def checkPrice():
    domain = getDomain()
    if domain == 'jumia':
        return jumiaPrice()
    else:
        return souqPrice()


def checkBudget():
    price=checkPrice()
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
