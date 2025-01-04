from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from .models import Car

class CarsMainPage(ListView):
    template_name = "cars_manager/main_page.html"
    model = Car
    context_object_name = 'cars'
    extra_context = {'title': 'Авто-мир'}


# Create your views here.
class TestView(TemplateView):
    template_name = "cars_manager/base.html"