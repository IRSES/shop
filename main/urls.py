from django.urls import path
from . import views
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('description/<int:product_id>', views.description, name='description'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('table/', ProductListView.as_view(), name='table'),
    path('product/new/', ProductCreateView.as_view(), name='product_new'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    #reg,log,logout
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user/profile/', views.user_profile, name='user_profile'),
    path('manage_permissions/<int:user_id>/', views.manage_user_permissions, name='manage_user_permissions'),
    # reset
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
