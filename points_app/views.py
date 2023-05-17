from django.shortcuts import render
from rest_framework.views import APIView
from .models import Point, ClosestPoints
from .serializers import PointSerializer, ClosestPointsSerializer
from rest_framework.response import Response




def calculate_distance(point1, point2):
    # distance calculations
    x1, y1 = map(int, point1.points.split(','))
    x2, y2 = map(int, point2.points.split(','))
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance



class ClosestPointsAPIView(APIView):




    def post(self, request, format=None):
        points_str = request.data['points']
        points_list = points_str.split(';')

        # Create Point objects and save them
        point_objects = []
        for point_str in points_list:
            point = Point(points=point_str)
            point.save()
            point_objects.append(point)

        # get closest points
        closest_points = []
        for i in range(len(point_objects)):
            closest_point = None
            min_distance = float('inf')

            for j in range(len(point_objects)):
                if i != j:
                    distance = calculate_distance(point_objects[i], point_objects[j])
                    if distance < min_distance:
                        min_distance = distance
                        closest_point = point_objects[j]

            if closest_point:
                closest_points.append((point_objects[i], closest_point))

        # Save closest points in ClosestPoints model
        for original_point, closest_point in closest_points:
            closest_points_obj = ClosestPoints(original_points=original_point, closest_point=closest_point)
            closest_points_obj.save()

        # Serialize the closest points and return the response
        serializer = ClosestPointsSerializer(closest_points_obj)
        return Response(serializer.data)
