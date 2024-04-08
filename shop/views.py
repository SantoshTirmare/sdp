from django.shortcuts import render
from .models import Product
from math import ceil
from django.http import HttpResponse


def index(request):
    """products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))"""
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("we are at Contact Us Page")


def tracker(request):
    return HttpResponse("we are at traking Status Page")


def search(request):
    return HttpResponse("we are at search Page")


def productView(request):
    return HttpResponse("we are at product View Page")


def checkout(request):
    return HttpResponse("we are at checkout page")
