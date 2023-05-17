from django.db import models

# Create your models here.

class Point(models.Model):
    points = models.CharField(max_length=200)

class ClosestPoints(models.Model):
    original_points = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='original_points')
    closest_point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='closest_point')
