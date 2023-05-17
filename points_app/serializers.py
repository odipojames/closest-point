from rest_framework import serializers
from .models import Point, ClosestPoints

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ('id', 'points')

class ClosestPointsSerializer(serializers.ModelSerializer):
    original_points = PointSerializer()
    closest_point = PointSerializer()

    class Meta:
        model = ClosestPoints
        fields = ('original_points', 'closest_point')
