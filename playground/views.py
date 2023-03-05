from django.shortcuts import render
from store.models import Product,Collection
from django.db.models import Q,F,Count,Max,Min,Value,Func,CharField,ExpressionWrapper,FloatField
from django.db.models.functions import Concat
from django.db import transaction


def say_hello(request):
    with transaction.atomic():
        Product.objects.filter(pk__range=(852,855)).delete()
        Collection.objects.filter(pk=16)




    return render(request, 'hello.html',{'name':'Waqar'})
                                        #  ,'result':list(queryset)})