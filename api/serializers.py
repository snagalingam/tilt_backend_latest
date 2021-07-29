from rest_framework import serializers
from users.models import User, UserDetail


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ('customer', 'unique_id', 'preferred_name', 'program')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    detail = UserDetailSerializer(required=True)

    class Meta:
        model = User
        fields = ('email', 'detail')
