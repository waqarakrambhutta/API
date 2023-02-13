from rest_framework import serializers
from decimal import Decimal
from store.models import Product,Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','description','unit_price','title','inventory','price_with_tax','collection']
        
    price_with_tax=serializers.SerializerMethodField(method_name='include_tax')
    def include_tax(self,product):
        return product.unit_price * Decimal(1.1)
    



    
    