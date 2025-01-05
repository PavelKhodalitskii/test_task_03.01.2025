from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from cars_manager.models import Car
from .serializers import CarBaseSerializer

# Create your views here.

class CarsListApiView(APIView):
    serializer_class = CarBaseSerializer

    def get(self, request, car_id=None | int):
        cars = Car.objects.all()
        return Response({
            "cars": self.serializer_class(cars, many=True).data
        })

class CarApiView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CarBaseSerializer

    def post(self, request):
        pass

    def put(self, request):
        pass
    
    def delete(self, request):
        pass