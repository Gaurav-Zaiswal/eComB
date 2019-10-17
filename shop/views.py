from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import math
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm
    return render(request, 'user/register.html', {'form': form})

def index(request):
    products = Product.objects.all()
    n = len(products)
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
        allProds.append([prod, range(nSlides), nSlides])
    context = {'allProds':allProds}

    # context = {
    #     'totalslides':slides,
    #     'range': range(2, slides), # because slide 0 is already active by default
    #     'product':products,  
    # }
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
