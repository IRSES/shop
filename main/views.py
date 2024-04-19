from django.db.models import Q
from .models import *
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


def home(request):
    products = Product.objects.all()
    context = {'products': products}

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        if not name or not email:
            messages.error(request, 'Имя и Email не могут быть пустыми.')
            return render(request, 'main/home.html', context)

        if FormData.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с таким email уже существует.')
            return render(request, 'main/home.html', context)

        try:
            new_user = FormData(name=name, email=email)
            new_user.full_clean()
            new_user.save()
            return redirect('home')
        except ValidationError as e:
            messages.error(request, '; '.join(e.messages))
        except Exception as e:
            messages.error(request, str(e))

    return render(request, 'main/home.html', context)


def about(request):
    return render(request, 'main/about.html')


def description(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_description = product.short_description
    return render(request, 'main/description.html', {'product': product, 'product_description': product_description})


def search(request):
    query = request.GET.get('query')
    if query:
        products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        context = {'search_results': products}
    else:
        context = {}
    return render(request, 'main/base.html', context)


#Другий варіант використання формування списку «об'єктів» предметної області та відправлення його на клієнтський комп'ютер. В результаті цього всі дані, збережені раніше, завантажуються з бази даних та відображується у табличному вигляді на відповідній Web- сторінці.
class ProductListView(ListView):
    model = Product
    template_name = 'main/table.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'main/product_form.html'
    success_url = '/table/'
    fields = ('title', 'description', 'price', 'image', 'short_description')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'main/product_edit_form.html'
    success_url = '/table/'
    fields = ('title', 'description', 'price', 'image', 'short_description')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'main/product_confirm_delete.html'
    success_url = '/table/'