from rest_framework import serializers
from .models import Collection,Product,Reviews


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
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','unit_price','inventory','collection']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id','product','name','description','date']

















































# from rest_framework import serializers
# from decimal import Decimal
# from store.models import Product,Collection

# class CollectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Collection
#         fields = ['id','title','featured_product']


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['id','description','unit_price','title','inventory','price_with_tax','collection']
        
#     price_with_tax=serializers.SerializerMethodField(method_name='include_tax')
#     def include_tax(self,product):
#         return product.unit_price * Decimal(1.1)
    



    
    