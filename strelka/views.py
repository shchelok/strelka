from django.http import HttpResponse
from django.shortcuts import render

from .models import Cart, Money
from django.utils import timezone

import requests
import json

def index(request):
    for cart in Cart.objects.all()[:]:
        balance = cart.checkCart()
        if balance != cart.carts.last().money :
            Money.objects.create(money=balance, update_date=timezone.now(), statMoney=cart)
    context = {'carts':Cart.objects.all()[:],}
    return render(request, 'strelka/index.html', context)

def balance(request, n):
    balance = '11'
    balance = Cart.objects.filter(number_card=n)[0].checkCart()
    context = {"balance": balance}
    return render(request, 'strelka/balance.html', context)


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
