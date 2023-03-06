from django.shortcuts import render
from store.models import Product,Collection,Order,OrderItem
from django.db.models import Q,F,Count,Max,Min,Value,Func,CharField,ExpressionWrapper,FloatField
from django.db.models.functions import Concat
from django.db import transaction


def say_hello(request):
    with transaction.atomic():
        order = Order()
        order.customer_id= 1
        order.save()

        item =  OrderItem()
        item.order_id=1
        item.unit_price=1
        item.quantity= 4
        item.product_id =1 
        item.save()



    return render(request, 'hello.html',{'name':'Waqar'})
                                        #  ,'result':list(queryset)})