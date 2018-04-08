#!/usr/bin/env python
# coding: utf8

import psycopg2
import requests
import json
from send_mail import send_mail

# CONF
HOST = "127.0.0.1"
PORT = "5432"
DATABASE = "django"
USER = "django"
PASSWORD = "arti04sQ3"

##
def getNumbers():
	conn = psycopg2.connect("dbname={0} user={1} password={2} host={3} port={4}".format(DATABASE, USER, PASSWORD, HOST, PORT))
	cur = conn.cursor()
	cur.execute("SELECT number_card, email, id, name_card from strelka_cart;")
	l = cur.fetchall()
	cur.close()
	return l



dataList = getNumbers()
for i in dataList:
	number_card = i[0]
	balance = requests.Session().get(
        'https://strelkacard.ru/api/cards/status/?cardnum={}&cardtypeid=3ae427a1-0f17-4524-acb1-a3f50090a8f3'.format(number_card)
            ).content
	balance = json.loads(balance.decode("utf8"))['balance']
	conn = psycopg2.connect("dbname={0} user={1} password={2} host={3} port={4}".format(DATABASE, USER, PASSWORD, HOST, PORT))
	cur = conn.cursor()
	cur.execute('select money from strelka_money WHERE "statMoney_id"={0} ORDER BY update_date  DESC limit 1;'.format(i[2]))
	last_date_balance = cur.fetchall()
	cur.close()
#	if float(balance)/100 < 50 and float(balance)/100 != float(last_date_balance[0][0]):
	send_mail(["{0}".format(i[1])], "Strelka", i[3], str(float(balance)/100), i[0])