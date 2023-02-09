from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from rest_framework import status
from .serializers import ProductSerializer
# Create your views here.

@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)
 
@api_view()
def product_detail(request,id):
    product=get_object_or_404(Product,pk=id)
    serializers = ProductSerializer(product)
    return Response(serializers.data)

    
    
    
# def product_detail(request,id):
#     try:
#             product=Product.objects.get(pk=id)
#             serializers = ProductSerializer(product)
#             return Response(serializers.data)
#     except Product.DoesNotExist:
#          return Response(status=status.HTTP_404_NOT_FOUND)


# def product_detail(request,id):
#     product=Product.objects.get(pk=id)
#     serializers = ProductSerializer(product)
    
#     return Response(serializers.data)