from django.conf.urls import url
#from django.conf.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^balance/(?P<n>\w+)$', views.balance),
    url(r'^history/(?P<n>\w+)$', views.history),
]