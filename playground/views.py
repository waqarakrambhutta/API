from django.shortcuts import render
from store.models import Product,Collection,Order,OrderItem
from django.db.models import Q,F,Count,Max,Min,Value,Func,CharField,ExpressionWrapper,FloatField
from django.db.models.functions import Concat
from django.db import transaction,connection


def say_hello(request):
    cursor = connection.cursor()
    cursor.execute('INSERT INTO store_collection (id,title) VALUES (14,"tube well")')
    cursor.close()

    # return render(request, 'hello.html',{'name':'Waqar','result':list(queryset)})
    return render(request, 'hello.html',{'name':'Waqar'})