from django.shortcuts import render
from django.db.models import F
from store.models import Product


def say_hello(request):
    queryset = Product.objects.all()[0:5]

    return render(request, 'hello.html', {'name': 'Tanner', 'products': queryset})