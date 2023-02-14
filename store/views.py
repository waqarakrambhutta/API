from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CollectionSerializer
from .models import Collection
from rest_framework import status


@api_view(['GET','POST'])
def collection_list(request):
    if request.method == 'GET':
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['GET','PATCH','DELETE'])
def collection_detail(request,id):
    collection = Collection.objects.get(pk=id) 
    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
               
























































# from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Product,Collection
# from rest_framework import status
# from .serializers import ProductSerializer,CollectionSerializer
# # Create your views here.

# @api_view(['GET','POST'])
# def collection_list(request):
#     if request.method == 'GET':
#         collection = Collection.objects.all()
#         serializer = CollectionSerializer(collection, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CollectionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data)
    

# @api_view(['GET','PATCH'])
# def collection_detail(request,id):
#     collection = get_object_or_404(Collection,pk=id)
#     if request.method=='GET':
#         serailizer = CollectionSerializer(collection)
#         return Response(serailizer.data)
#         # return Response()
#     elif request.method=='PATCH':
#         serailizer=CollectionSerializer(data=request.data)
#         serailizer.is_valid(raise_exception=True)
#         serailizer.save()
#         return Response(serailizer.data)
#     # return Response('ok')


# @api_view(['GET','POST'])
# def product_list(request):
#     if request.method == 'GET':
#         queryset = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(
#             queryset, 
#             many=True,
#             context={'request':request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
        


# @api_view(['GET','PATCH','DELETE'])
# def product_detail(request,id):
#     product=get_object_or_404(Product,pk=id)
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         serializer = ProductSerializer(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         if product.orderitem_set.count()>0:
#             return Response({'errors':'Product cannot be created because it is associated with orderitem.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


    
 