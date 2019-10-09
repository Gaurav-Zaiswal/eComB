from django.urls import path
from .import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('login/', LoginView, {'template_naem': 'authentication/login.html'}),
    path('', views.index, name ='Index'),
    path('home/', views.index, name = 'home'),
    path('contactus/', views.contact, name = 'ContactUs'),
    path('about/', views.about, name = 'AboutUs'),
    path('tracker/', views.tracker, name = 'Tracker'),
    path('preview/', views.productpreview, name = 'Product_preview'),
    path('cart/', views.cart, name = 'Cart'),
    path('search/', views.search, name = 'Search'),
    path('checkout/', views.checkout, name = 'Checkout'),
    path('log-in/', views.log_in, name = 'Login'),
    path('logout/', views.log_out, name = 'Logout'),
    path('register/', views.register, name = 'Register'),
    path('change-pass/', views.changePass, name = 'ChangePass'),
]   