from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name ='Index'),
    path('home/', views.index, name = 'home'),
    path('contactus/', views.contact, name = 'ContactUs'),
    path('about/', views.about, name = 'AboutUs'),
    path('tracker/', views.tracker, name = 'Tracker'),
    path('preview/', views.productpreview, name = 'Product_preview'),
    path('cart/', views.cart, name = 'Cart'),
    path('search/', views.search, name = 'Search'),
    path('checkout/', views.checkout, name = 'Checkout'),
    path('login/', views.login, name = 'Login'),
    path('logout/', views.logout, name = 'Logout'),
    path('register/', views.register, name = 'Register'),
    path('change-pass/', views.changePass, name = 'ChangePass'),
]   