from django.urls import path

from .views import CarsMainPage, CarsDetailsView, CarsFormView, delete_comment

urlpatterns = [
    path('', CarsMainPage.as_view(), name='main_page'),
    path('create/', CarsFormView.as_view(), name='car_create'),
    path('update/<int:car_id>/', CarsFormView.as_view(), name='car_update'),
    path('details/<int:car_id>/', CarsDetailsView.as_view(), name='car_details'),
    path('commment/create/<int:car_id>', CarsDetailsView.as_view(), name='post_comment'),
    path('commment/delete/<int:comment_id>', delete_comment, name='delete_comment')
]