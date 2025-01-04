from django.urls import path

from .views import CarsMainPage, CarsDetailsView, delete_comment

urlpatterns = [
    path('', CarsMainPage.as_view(), name='main_page'),
    path('details/<int:car_id>/', CarsDetailsView.as_view(), name='car_details'),
    path('commment/create/<int:car_id>', CarsDetailsView.as_view(), name='post_comment'),
    path('commment/delete/<int:comment_id>', delete_comment, name='delete_comment')
]