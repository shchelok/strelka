from django import forms

from .models import Cart

import requests
import json

class CartForms(forms.Form):
	cartNumber = CharField(widget=forms.Textarea)
	checkCart = BooleanField(initial='false')

	def checkCart():
		ses = requests.Session()
		n = req.get('https://strelkacard.ru/api/cards/status/?cardnum={}&cardtypeid=3ae427a1-0f17-4524-acb1-a3f50090a8f3'.format(cartNumber))
		balance = json.loads(n.content)['balance']
		return balance

	if checkCart == True:
		money = checkCart()
		c = Cart.objects.get(number_card=cartNumber)
		c.money.money = balance
		c.save()