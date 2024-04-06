from django.shortcuts import render
from django.db.models import Q
from .models import *


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'main/home.html', context)


def about(request):
    return render(request, 'main/about.html')


def search(request):
    query = request.GET.get('query')
    if query:
        products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        context = {'search_results': products}
    else:
        context = {}
    return render(request, 'main/base.html', context)
