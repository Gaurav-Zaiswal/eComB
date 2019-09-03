from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    products = Product.objects.all
    context = {
        'products':products,
    }
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
    return HttpResponse('this is shop chockupt point page')
