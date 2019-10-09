from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name ='Index'),
    path('home/', views.index, name = 'home'),
    path('contactus/', views.contact, name = 'ContactUs'),
    path('about/', views.about, name = 'AboutUs'),
    path('tracker/', views.tracker, name = 'Tracker'),
    path('preview/', views.productpreview, name = 'Product_preview'),
    path('search/', views.search, name = 'Search'),
    path('checkout/', views.checkout, name = 'Checkout'),
    
]   