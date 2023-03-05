from django.shortcuts import render
from store.models import Product,Collection
from django.db.models import Q,F,Count,Max,Min,Value,Func,CharField,ExpressionWrapper,FloatField
from django.db.models.functions import Concat


def say_hello(request):
    queryset = Product.objects.filter(pk__range=(900,1001)).delete()


    return render(request, 'hello.html',{'name':'Waqar','result':list(queryset)})