from django.shortcuts import render
from .models import *


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'main/home.html', context)


def about(request):
    return render(request, 'main/about.html')