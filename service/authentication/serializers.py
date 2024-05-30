from rest_framework import serializers
from .models import CustomUser



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','name', 'email', 'password', 'phone_number', 'birth_date']
        extra_kwargs = {'password': {'write_only': True}}
