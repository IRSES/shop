# admin.py

from django.contrib import admin
from .models import Product
from .models import FormData
from .models import ProductDescription

admin.site.register(FormData)

admin.site.site_header =  "The FLower Shop" # Заголовок

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')  # Поля, які відображаються у списку
    ordering = ('title', 'price')  # Поля для сортування

admin.site.register(Product, ProductAdmin) 

class ProductInline(admin.StackedInline):
    model = Product # Вказуємо модель, яку будемо відображати
    extra = 0  # Вказуємо кількість додаткових блоків для введення

class ProductDescriptionAdmin(admin.ModelAdmin):
    model = ProductDescription # Вказуємо модель, яку будемо налаштовувати
    inlines = [ProductInline]  # Включаємо вкладений клас ProductInline

admin.site.register(ProductDescription, ProductDescriptionAdmin)