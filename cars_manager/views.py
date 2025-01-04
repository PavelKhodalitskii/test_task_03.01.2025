from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView

from .models import Car

class CarsMainPage(ListView):
    template_name = "cars_manager/main_page.html"
    model = Car
    context_object_name = 'cars'
    extra_context = {'title': 'Авто-мир'}

class CarsDetailsView(DetailView):
    template_name = "cars_manager/car_details.html"
    model = Car
    context_object_name = 'car'
    pk_url_kwarg = 'car_id'

class TestView(TemplateView):
    template_name = "cars_manager/base.html"