from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import math

def index(request):
    products = Product.objects.all()
    n = len(products)
    slides = n // 4 + math.ceil(n/4 - n//4)
    context = {
        'totalslides':slides,
        'range': range(1, slides), # because slide 0 is already active by default
        'product':products,  
    }
    # print(context)
    return render(request, 'shop/index.html', context)

def about(request):
    return render(request, 'shop/aboutus.html')
def contact(request):
    return HttpResponse('this is shop contact us page')

def tracker(request):
    return HttpResponse('this is shop tracker page')

def search(request):
    return HttpResponse('this is shop search page page')

def productpreview(request):
    return HttpResponse('this is shop product preview page')

def checkout(request):
    return HttpResponse('this is shop checkout point page')
