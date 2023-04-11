from decimal import Decimal
from django.db import transaction
from rest_framework import serializers
from .models import Collection,Product,Review,Cart,CartItem,Customer,Order,OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','unit_price','collection']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    totalprice = serializers.SerializerMethodField()

    def get_totalprice(self,cart_item:CartItem):
        return cart_item.quantity * cart_item.product.unit_price

    class Meta:
        model= CartItem
        fields=['id','product','quantity','totalprice']

class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True,read_only=True)
    #write any existing field equal to serializer of any other model.
    total_price = serializers.SerializerMethodField()
    
    def get_total_price(self,cart):
        return sum([item.quantity * item.product.unit_price for item in cart.items.all()])

    class Meta:
        model = Cart
        fields = ['id','items','total_price']

class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self,value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError('No product with given id was found.')
        return value

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']
        # now save it.
        try:  
            cart_item=CartItem.objects.get(cart_id=cart_id,product_id=product_id)
            # if there's no cart item it will through the exception.
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
            # instance is the built in variable in the save method of the ModelSerializer.

        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id,**self.validated_data)

        return self.instance


    class Meta:
        model = CartItem
        fields = ['id','product_id','quantity']

class UpdateCartitemSerializer(serializers.ModelSerializer):
    class Meta:
        model= CartItem
        fields = ['quantity']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Collection
        fields = ['id','title','product_count']

    product_count = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        serializer = Collection(**validated_data)
        serializer.other = 1
        serializer.save()
        return serializer
    



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','name','description','date']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id,**validated_data)

class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True )
   
    class Meta:
        model = Customer
        fields = ['id','user_id','phone','birth_date','membership']

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','unit_price']


class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    class Meta:
        model = OrderItem
        fields = ['product','quantity','unit_price']

class OrderSerializer(serializers.ModelSerializer):
    item = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id','placed_at','payment_status','customer_id','item']

class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['payment_status']
    

class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self,cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('NO, cart with the given id was found...')
        if CartItem.objects.filter(cart_id=cart_id).count()==0:
            raise serializers.ValidationError('The cart is empty...')
        return cart_id
    
    def save(self, **kwargs):
        with transaction.atomic():
            cart_id = self.validated_data['cart_id']
            
            customer = Customer.objects.get(user_id = self.context['user_id'])
            order = Order.objects.create(customer=customer)

            cart_items  =  CartItem.objects.filter(cart_id=cart_id)     

            # the format is [items for items in collection]
            order_items = [
                OrderItem(
                order= order,
                product = item.product,
                unit_price= item.product.unit_price,
                quantity = item.quantity
                ) 
                for item in cart_items
            ]
            OrderItem.objects.bulk_create(order_items)

            Cart.objects.filter(pk=cart_id).delete()
            return order



















# from rest_framework import serializers
# from decimal import Decimal
# from store.models import Product,Collection

# class CollectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Collection
#         fields = ['id','title','featured_product']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','description','unit_price','title','inventory','price_with_tax','collection']
        
    price_with_tax=serializers.SerializerMethodField(method_name='include_tax')
    def include_tax(self,product):
        return product.unit_price * Decimal(1.1)
    



    
    