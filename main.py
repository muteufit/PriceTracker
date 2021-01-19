from modules.user_budget import UserBudget
from modules.website_controller import WebsiteController
from modules.send_mail import MailSender
from time import sleep


def main():
    url = input('Product Url => ')
    webc = WebsiteController(url)
    budget = int(input('Your Budget (Numbers) => '))
    up = UserBudget(budget)
    while True:
        op = webc.getPrice()
        compare = up.compare(op)
        if compare[0]:
            ms = MailSender('sender@example.com', '******',
                            'reciever@example.com')
            ms.sendMail('you can buy it now',
                        'save up to {}'.format(compare[1]), 'alternate')
            break
        print('==================================')
        print('= You Need {} more To Buy.'.format(compare[1]))
        print('= We\'re Trying Again in an Hour ')
        print('==================================')
        sleep(3600)


if __name__ == "__main__":
    main()
