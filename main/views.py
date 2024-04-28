from django.db.models import Q
from .models import *
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .forms import UserProfileForm


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


# reg
@login_required
def user_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'main/user_profile.html', {'form': form, 'user': user})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('home')


@login_required 
def manage_user_permissions(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)  # Получаем объект пользователя или 404 ошибку, если пользователь не найден
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile', user_id=user_id)
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'main/manage_user_permissions.html', {'form': form})