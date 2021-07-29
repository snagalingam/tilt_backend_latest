from rest_framework import serializers
from users.models import CustomerUser


class CustomerUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = ('unique_id','preferred_name','program')
