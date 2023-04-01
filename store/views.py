from .serializers import CartSerializer,CartItemSerializer,AddCartItemSerializer,UpdateCartitemSerializer,ProductSerializer,CollectionSerializer,ReviewSerializer,CustomerSerializer,OrderSerializer,CreateOrderSerializer
from .models import Cart,CartItem,Product,OrderItem,Collection,Review,Customer,Order
from rest_framework.decorators import api_view
from django.http import request
from .pagination import DefaultPagination
from .filters import ProductFilter
from django.db.models import Count
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.generics import RetrieveAPIView,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,IsAdminUser
from store.permissions import IsAdminOrReadOnly,FullDjangoModelPermissions, ViewCustomerHistoryPermission

class CollectionViewSets(ModelViewSet):
    queryset = Collection.objects.annotate(product_count=Count('product')).all()
    serializer_class = CollectionSerializer
    permission_classes = [DjangoModelPermissions]

    def destroy(self, request, *args, **kwargs):
        product = Collection.objects.annotate(product_count=Count('product')).get(pk=id) 
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return super().destroy(request, *args, **kwargs)

class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends =[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['title','description']
    ordering_fields = ['unit_price','last_update']

    def get_serializer_context(self):
        return {'request':self.request}
    
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count()>0:
            return Response({'errors':'Product cannot be created because it is associated with orderitem.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

class CartViewset(ListCreateAPIView,
                  CreateModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewset(ListCreateAPIView,
                      CreateModelMixin,
                      RetrieveModelMixin,
                      DestroyModelMixin,
                      GenericViewSet):
    
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

# def CartItem_list(request):
#     return Response('ok')

    
class CartItemVeiwSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete']
    #To prevent put request along with the patch method.
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartitemSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {'cart_id':self.kwargs['cart_pk']}

    def get_queryset(self):
        return CartItem.objects.select_related('product').filter(cart_id=self.kwargs['cart_pk'])


class ReviewViewset(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}

class CustomerViewset(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True,permission_classes=[ViewCustomerHistoryPermission])
    def history(self,request,pk):
        return Response('ok')

    @action(detail=False,methods=['GET','PUT'])
    def me(self,request): # the user has the user_id the middleware in the setting who inspect the user and attach the user from the database.
        (customer,created) = Customer.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer,data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        
class OrderViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        return OrderSerializer

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
    

    def get_queryset(self):
        user= self.request.user

        if user.is_staff:
            return Order.objects.all()
        (customer_id, created)= Customer.objects.only('id').get_or_create(user_id=user.id)
        return Order.objects.filter(customer_id = customer_id)









# from django.shortcuts import get_object_or_404
# from django_filters.rest_framework import DjangoFilterBackend
# from django.db.models import Count
# from rest_framework.filters import SearchFilter,OrderingFilter
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# from rest_framework.views import APIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.pagination import PageNumberPagination
# from rest_framework import status
# from .pagination import DefaultPagination
# from .filters import ProductFilter
# from .serializers import CollectionSerializer,ProductSerializer,ReviewSerializer
# from .models import Collection,Product,OrderItem,Review



  
   

    



# class ProductList(ListCreateAPIView):
#     queryset = queryset = Product.objects.select_related('collection').all()
#     serializer_class = ProductSerializer

#     def get_serializer_context(self):
#         return {'request':self.request}

# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def delete(self, request,pk):
#         product = get_object_or_404(Product,pk=pk)
#         if product.orderitem_set.count()>0:
#             return Response({'errors':'Product cannot be created because it is associated with orderitem.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        

               


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