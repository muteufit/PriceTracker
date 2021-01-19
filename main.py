from modules.user_budget import UserBudget
from modules.website_controller import WebsiteController
from modules.send_mail import MailSender


def main():
    url = input('Product Url => ')
    webc = WebsiteController(url)
    budget = int(input('Your Budget (Numbers) => '))
    up = UserBudget(budget)
    while:
        op = webc.getPrice()
        compare = UserBudget.compare(op)
        if compare[0]:
            ms = MailSender('sender@example.com', '******',
                            'reciever@example.com')
            ms.sendMail('you can buy it now',
                        'save up to {}'.format(compare[1]), 'alternate')
            break


if __name__ == "__main__":
    main()