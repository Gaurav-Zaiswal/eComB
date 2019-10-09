from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import math
from django.contrib.auth.decorators import login_required

# def login(request):
#     return render(request, 'authorization/login.html')

def logout(request):
    return render(request, 'authorization/logout.html')

def register(request):
    return render(request, 'authorization/register.html')

def changePass(request):
    return render(request, 'authorization/change_pass.html')

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

@login_required
def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return HttpResponse('this is shop search page page')

def productpreview(request):
    return HttpResponse('this is shop product preview page')

@login_required
def checkout(request):
    return render(request, 'shop/checkout.html')


def cart(request):
    return render(request, 'shop/cartlist.html')
