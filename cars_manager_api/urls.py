from django.urls import path
from .views import CarApiView, CarsListApiView


urlpatterns = [
    path('cars/', CarsListApiView.as_view(), name="api_cars_list"),
]