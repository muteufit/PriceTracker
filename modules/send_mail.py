import smtplib
from email.message import EmailMessage


class MailSender:
    def __init__(self, senderAddress, senderPassword, recieverAddress):
        self.senderAddress = senderAddress
        self.senderPassword = senderPassword
        self.recieverAddress = recieverAddress

    def sendMail(self, subject, content, alternate):
        msg = EmailMessage()
        # set your email address
        msg['From'] = self.senderAddress
        # set your friend email address
        msg['To'] = self.recieverAddress
        # set subject
        msg['Subject'] = subject
        # set the body
        msg.set_content(content)
        msg.add_alternative(alternate, subtype='html')
        # better methode than SMTP
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            # login with your email and password
            smtp.login(self.senderAddress, self.senderPassword)
            # send the message
            smtp.send_message(msg)
