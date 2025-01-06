from django.shortcuts import redirect
from django.contrib.auth import logout, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import UserRegistrationForm
from .service import UserController


class LoginUser(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('root')

class RegisterUser(FormView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        # Устновим пользователю стандартную группу разрешений
        UserController.set_group(new_user, 'default_user')
        login(request=self.request, user=new_user)
        return redirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('root')

def logout_user(request):
    logout(request)
    return redirect('login')