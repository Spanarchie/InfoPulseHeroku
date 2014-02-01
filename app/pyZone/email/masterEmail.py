'''
Created on 22 Jan 2014

@author: Colin Moore-Hill
'''
#! /usr/bin/python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from templates import RegistrationMail


# Credentials (if needed)
username = 'infopulsecouk'
password = 'Wolf3105'
# me == my email address
# you == recipient's email address
me = 'infopulsecouk@gmail.com'
you = 'spanarchiantesting@gmail.com, itestedthis1@gmail.com'


def sendEmail():
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Welcome to infopulsecouk"
    msg['From'] = me
    msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
    html = RegistrationMail.getRegHtml()

# Record the MIME types of both parts - text/plain and text/html.
#part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
#msg.attach(part1)
    msg.attach(part2)

# Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    print("Starting Server....!")
    s.login(username,password)
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
    s.sendmail(me, you, msg.as_string())
    s.quit()

if __name__ == '__main__':
    sendEmail()

