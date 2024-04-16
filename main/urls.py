from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('table/', views.product_list, name='table'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),


    # path('submit-data/', views.submit_data, name='submit_data'),
]
