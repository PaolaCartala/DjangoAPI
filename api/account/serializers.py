from rest_framework import serializers

from account.models import CustomUser


# CustomUser
class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id', 'username', 'first_name', 'last_name',
            'email', 'address', 'phone'
        )
