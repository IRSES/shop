from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('description/<int:product_id>', views.description, name='description'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('table/', views.product_list, name='table'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]

