from rest_framework import serializers
from .models import RecyclingCompany, CollectionPoints, CollectsNeighborhoods


class RecyclingCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecyclingCompany
        fields = '__all__'


class CollectionPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionPoints
        fields = '__all__'


class CollectsNeighborhoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectsNeighborhoods
        fields = '__all__'