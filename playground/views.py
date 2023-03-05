from django.shortcuts import render
from store.models import Product


def say_hello(request):
    product = Product.objects.filter(id=5).first()

    return render(request, 'hello.html',{'name':'Waqar'})
