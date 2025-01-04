from django.urls import path

from .views import TestView, CarsMainPage

urlpatterns = [
    path('', CarsMainPage.as_view(), name='main_page'),
]