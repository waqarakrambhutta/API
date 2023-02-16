from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import CollectionSerializer,ProductSerializer
from rest_framework.decorators import api_view
from .models import Collection,Product
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.db.models import Count


class CollectionViewSets(ModelViewSet):
    queryset = Collection.objects.annotate(product_count=Count('product')).all()
    serializer_class = CollectionSerializer
    def delete(self,request,pk):
        collection = Collection.objects.annotate(product_count=Count('product')).get(pk=pk) 
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   




class ProductList(ListCreateAPIView):
    queryset = queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request':self.request}

class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request,pk):
        product = get_object_or_404(Product,pk=pk)
        if product.orderitem_set.count()>0:
            return Response({'errors':'Product cannot be created because it is associated with orderitem.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

               


# @api_view(['GET','POST'])
# def product_list(request):
#     if request.method == 'GET':
        
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


        




    
 
# @api_view(['GET','PATCH','DELETE'])
# def collection_detail(request,id):
#     collection = Collection.objects.annotate(product_count=Count('product')).get(pk=id) 
#     if request.method == 'GET':
#         serializer = CollectionSerializer(collection)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         serializer = CollectionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)