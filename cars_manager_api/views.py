from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.mixins import CreateModelMixin
from rest_framework.exceptions import NotAuthenticated

from cars_manager.models import Car, Comment
from .serializers import CarBaseSerializer, CarDetailSerializer, CommentsBaseSerializer
from .permissions import IsOwnerOrReadOnly


class CarsListCreateApiView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CarBaseSerializer
        # Для GET запросов - детальное представление информации об автомобиях
        return CarDetailSerializer

    def perform_create(self, serializer):
        # Устанавливаем владельца автомобилю
        serializer.save(owner=self.request.user)

class CarDetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    lookup_field = 'id'
    
    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return CarBaseSerializer
        # Для GET запросов - детальное представление информации об автомобиле
        return CarDetailSerializer
    
class CommentDetailCreateViewApiView(generics.ListAPIView, CreateModelMixin):
    serializer_class = CommentsBaseSerializer

    def get_queryset(self):
        # Возвращает комментарии по id автомобиля
        car_id = self.kwargs.get('id')
        return Comment.objects.filter(car__id=car_id)
    
    # Реализация post метода для CreateModelMixin
    def post(self, request, *args, **kwargs):
        if not request.user:
            raise NotAuthenticated("Не аутентицифированный запрос", code=403)
        return self.create(request, *args, **kwargs)
    