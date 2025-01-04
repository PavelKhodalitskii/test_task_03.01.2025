from django.urls import path

from .views import TestView

urlpatterns = [
    path('', TestView.as_view(), name='main_page'),
]