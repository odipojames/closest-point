from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Point, ClosestPoints

class ClosestPointsAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_closest_points_api(self):
        url = reverse('points')
        data = {'points': '2,2;-1,30;20,11;4,5'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Point.objects.count(), 4)
        self.assertEqual(ClosestPoints.objects.count(), 1)
        closest_point = ClosestPoints.objects.first()
        self.assertEqual(str(closest_point), '2,2;4,5')
