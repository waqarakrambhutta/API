from django.shortcuts import render
from store.models import Product
from django.db.models import Q


def say_hello(request):
    queryset = Product.objects.filter(~Q(unit_price__gt=10)).first()


    return render(request, 'hello.html',{'name':'Waqar'})