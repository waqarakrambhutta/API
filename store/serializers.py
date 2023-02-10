from rest_framework import serializers
from decimal import Decimal
from store.models import Product,Collection


class ProductSerializer(serializers.Serializer):
    id= serializers.IntegerField()
    title  = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2,source='unit_price')
    unit_price_with_tax = serializers.SerializerMethodField(method_name='price_with_tax')

    def price_with_tax(self,product:Product):
        return product.unit_price * Decimal(1.1)
        

    
class CollectionSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    new_title =  serializers.SerializerMethodField(method_name='serialized')

    def serialized(self,collection:Collection):
        return 'THIS IS NEW TITLE: '+collection.title
    
    