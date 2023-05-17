from django.urls import path
from . import views


urlpatterns = [
path('api/points', views.ClosestPointsAPIView.as_view(),name="points"),
]
