from django.urls import path

from .views import LoginUser, logout_user

urlpatterns = [
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout")
]