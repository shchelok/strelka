from django.contrib import admin

from .models import Cart
from .models import Money

admin.site.register(Cart)
admin.site.register(Money)
