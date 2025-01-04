from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy


class LoginUser(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('root')

def logout_user(request):
    logout(request)
    return redirect('login')