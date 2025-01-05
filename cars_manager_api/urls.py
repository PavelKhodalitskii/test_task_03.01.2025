from django.urls import path
from .views import CarDetailUpdateDeleteApiView, CarsListCreateApiView, CommentDetailCreateViewApiView


urlpatterns = [
    path('cars/', CarsListCreateApiView.as_view()),
    path('cars/<int:id>', CarDetailUpdateDeleteApiView.as_view()),
    path('cars/<int:id>/comments/', CommentDetailCreateViewApiView.as_view())
]