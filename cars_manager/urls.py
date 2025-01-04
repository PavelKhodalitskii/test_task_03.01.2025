from django.urls import path

from .views import TestView, CarsMainPage, CarsDetailsView

urlpatterns = [
    path('', CarsMainPage.as_view(), name='main_page'),
    path('details/<int:car_id>/', CarsDetailsView.as_view(), name='car_details')
]