from djoser.serializers import UserSerializer as BaseUserSerializer,UserCreateSerializer as BaseUserCreateSerializer
from store.models import Customer

class UserCreateSerializer(BaseUserCreateSerializer):
    def save(self, **kwargs):
        user = super().save(**kwargs)
        Customer.objects.create(user=user)

    class Meta(BaseUserCreateSerializer.Meta):
        # model = User # we can also implement the user model instead of inheriting meta class.
        fields= ['id','username','email','password','first_name','last_name']

class CurrentUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id','email','username','first_name','last_name']        