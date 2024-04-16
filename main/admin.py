# admin.py

from django.contrib import admin
from .models import Product
from .models import FormData
from .models import ProductDescription


admin.site.register(Product)
admin.site.register(FormData)
admin.site.register(ProductDescription)
