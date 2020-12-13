import smtplib
from email.message import EmailMessage
from main import url

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
