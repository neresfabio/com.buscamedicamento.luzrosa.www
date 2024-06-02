from rest_framework import serializers
from .models import RemedyOrder, ExternalRemedyData, LocationUser



class RemedyOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemedyOrder
        fields = '__all__'

class LocationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationUser
        fields = ['city', 'region']

class ExternalRemedyDataSerializer(serializers.ModelSerializer):
    location = LocationUserSerializer()

    class Meta:
        model = ExternalRemedyData
        fields = ['title', 'snippet', 'link', 'image', 'location']

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location, created = LocationUser.objects.get_or_create(**location_data)
        validated_data['location'] = location
        return ExternalRemedyData.objects.create(**validated_data)