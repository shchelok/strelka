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
'''
Данный модуль принимает список аргументов recipients,copy,blind_copy,files,subject,text,warning_recipients
Отправляет письма адресатам (recipients,copy,blind_copy) с темой subject текстом письма text
'''


def send_mail(recipients,subject,text):
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
#	msg['cc'] = ', '.join( copy[0:] ) # отправка копии 1-му адресату
#	msg['bc'] = ', '.join( blind_copy[0:] ) # отправка копии 1-му скрытому адресату


	# Формируем письмо
    MIMEText(text.encode('utf-8'), 'plain')

	# Подключаемся к smtp серверу
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("shpalbl4a@gmail.com","n3n99lz76343")

	# Отправляем письмо
            
    s.quit()

#send_mail(recipients,copy,blind_copy,files,subject,text,warning_recipients)
#send_mail(['a.shchelok@gmail.com','shpalbl4a@gmail.com'],'Soon Happy birthday!','test',[],smtp_login,password)
send_mail(["a.shchelok@gmail.com"], "Test for carts checker", "Test")
