#!/usr/bin/env python
# coding: utf8

import smtplib, os, sys
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE, formatdate
from email import encoders
reload(sys)
sys.setdefaultencoding('utf8')


def send_mail(recipients,subject,name,balance,number_cart):
    toaddr = recipients

    reports_server = '<checkerCart>'
    you = 'To: ' + ', '.join(toaddr)
    blind_copy = ['a.shchelok@gmail.com']

	# Формируем заголовок письма
    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = reports_server
    msg['To'] = ', '.join( recipients[0::] ) # отправка 2-м адресатам
    msg['Date'] = formatdate(localtime = True)
    msg['bc'] = ', '.join( blind_copy[0:] ) # отправка копии 1-му скрытому адресату


    html = '''
        <html>
        <head></head>
            <body>
                <p>Hi Dr {0}!<br>
                    Your carts balance is {1}<br>
                    You can check the balance cart yourself <a href="{2}">Number the cart is {3}</a>
                </p>
            </body>
        </html>
    '''.format(name, balance,'https://strelkacard.ru/',number_cart )
	# Формируем письмо
    part1 = MIMEText(html,'html')
    msg.attach(part1)

	# Подключаемся к smtp серверу
    s = smtplib.SMTP("smtp.gmail.com", 587)#("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("*******@gmail.com","******")

	# Отправляем письмо
            
    s.sendmail(reports_server, toaddr, msg.as_string())
    s.quit()

#send_mail(["a.shchelok@gmail.com"], "Strelka", "Alisa","222.58","03339877728")
