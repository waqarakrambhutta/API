from rest_framework import serializers
from decimal import Decimal
from store.models import Product,Collection

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','unit_price','price_with_tax','collection']
        
    price_with_tax=serializers.SerializerMethodField(method_name='include_tax')
    def include_tax(self,product):
        return product.unit_price * Decimal(1.1)
    
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection-detail'
    )
        

    


    
    