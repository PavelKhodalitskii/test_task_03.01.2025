from django.urls import path

from .views import (CarsMainPage,
                    CarsDetailsView,
                    CarsDeleteView,
                    delete_comment,
                    CarsCreateFormView,
                    CarsUpdateFormView,
                    CommentCreateView)

urlpatterns = [
    path('', CarsMainPage.as_view(), name='main_page'),
    path('create/', CarsCreateFormView.as_view(), name='car_create'),
    path('update/<int:car_id>/', CarsUpdateFormView.as_view(), name='car_update'),
    path('delete/<int:car_id>/', CarsDeleteView.as_view(), name='car_delete'),
    path('details/<int:car_id>/', CarsDetailsView.as_view(), name='car_details'),
    path('comment/create/<int:car_id>', CommentCreateView.as_view(), name='post_comment'),
    path('comment/delete/<int:comment_id>', delete_comment, name='delete_comment')
]