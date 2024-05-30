from rest_framework import serializers
from .models import RemedyOrder



class RemedyOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemedyOrder
        fields = '__all__'
