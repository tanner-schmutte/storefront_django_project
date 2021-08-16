from django.shortcuts import render
from django.db.models import F
from store.models import Product


def say_hello(request):
    product = Product.objects.latest('unit_price')

    return render(request, 'hello.html', {'name': 'Tanner', 'product': product})