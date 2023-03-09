from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        # model = User # we can also implement the user model instead of inheriting meta class.
        fields= ['id','username','email','password','first_name','last_name']