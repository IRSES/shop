from django.urls import path
from . import views
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView


urlpatterns = [
    path('', views.home, name='home'),
    path('description/<int:product_id>', views.description, name='description'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('table/', ProductListView.as_view(), name='table'),
    path('product/new/', ProductCreateView.as_view(), name='product_new'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
