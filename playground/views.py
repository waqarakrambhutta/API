from django.shortcuts import render
from store.models import Product,Collection,Order,OrderItem
from django.db.models import Q,F,Count,Max,Min,Value,Func,CharField,ExpressionWrapper,FloatField
from django.db.models.functions import Concat
from django.db import transaction


def say_hello(request):
    queryset= Product.objects.raw('SELECT * FROM store_product\
                                  order by inventory')


    return render(request, 'hello.html',{'name':'Waqar','result':list(queryset)})