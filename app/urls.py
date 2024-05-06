from django.urls import path
from django.contrib.auth import views as auth_views

from app import admin
from .views import add_customer, signup_view, logout_view, add_product, add_shipping, home, dashboard

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', signup_view, name='signup'),
    
    path('dashboard/', dashboard, name='dashboard'), 
    path('dashboard/logout/', logout_view, name='logout'),  # Corrected URL pattern
    path('add-customer/', add_customer, name='add_customer'),
    path('add-product/', add_product, name='add_product'),
    path('add-shipping/', add_shipping, name='add_shipping'),
]
