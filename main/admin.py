# admin.py

from django.contrib import admin
from .models import Product
from .models import FormData

admin.site.register(Product)
admin.site.register(FormData)
