from django.db import models
from django.utils import timezone

import requests
import json

class Cart(models.Model):
#docstring for cart"models.Modelf __init__(self, arg):
#super(cart,models.Model.__init__()
#self.arg = arg"""
	url_strelka = models.CharField(max_length=200, verbose_name='URL')
	name_card = models.CharField(max_length=20, verbose_name='Имя владельца карты')
	number_card = models.CharField(max_length=11, verbose_name='Номер карты')
	created_date = models.DateTimeField(default=timezone.now)
	balance = models.CharField(max_length=6, verbose_name='Баланс карты', null = True, blank = True)
	email = models.EmailField(max_length=20, verbose_name='email', blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name_card

	def checkCart(self):
		balance = requests.Session().get(
            'https://strelkacard.ru/api/cards/status/?cardnum={}&cardtypeid=3ae427a1-0f17-4524-acb1-a3f50090a8f3'.format(self.number_card)
            ).content
		balance = json.loads(balance.decode("utf8"))['balance']
		#self.self()
		return balance/100

class Money(models.Model):
	money = models.FloatField(verbose_name='Кол-во денег на счету')
	update_date = models.DateTimeField(default=timezone.now)
	statMoney = models.ForeignKey(Cart, related_name='carts' ,null=True, on_delete = models.SET_NULL)
	def publish(self):
		self.published_date = timezone.now()
		self.save()