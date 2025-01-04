from django.shortcuts import get_object_or_404, redirect, render

from django.urls import reverse_lazy
from django.views.generic import (ListView, 
                                  DetailView, 
                                  FormView, 
                                  DeleteView)

from .forms import CommentForm, CarForm
from .models import Car, Comments
from .service import CarController, CommentsController


class CarsMainPage(ListView):
    template_name = "cars_manager/main_page.html"
    model = Car
    context_object_name = 'cars'
    extra_context = {'title': 'Авто-мир'}

class CarsFormView(FormView):
    template_name = 'cars_manager/base_form.html'
    form_class = CarForm
    success_url = "/"
    pk_url_kwarg = 'car_id'

    def get_object(self):
        object_pk = self.kwargs.get(self.pk_url_kwarg)
        if object_pk:
            return get_object_or_404(Car, id=object_pk)
        return None
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        car = self.get_object()
        if car:
            form = self.form_class(instance=car)
        return form
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        if car:
            context['action'] = 'Изменить'
        else:
            context['action'] = 'Создать'
        return context
    
class CarsDetailsView(DetailView):
    template_name = "cars_manager/car_details.html"
    model = Car
    context_object_name = 'car'
    pk_url_kwarg = 'car_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_comment_form'] = CommentForm()
        return context

    def post(self, request, *args , **kwargs):
        comment_form = CommentForm(self.request.POST)
        if comment_form.is_valid():
            content = comment_form.cleaned_data['content']
            parent = comment_form.cleaned_data.get('parent')

        new_comment = Comments(content=content, author = self.request.user, car=self.get_object(), parent=parent)
        new_comment.save()
        return redirect(self.request.path_info)

class CarsDeleteView(FormView):
    pass

def delete_comment(request, comment_id):
    comment = CommentsController.get_comment(id=comment_id)
    if comment:
        CommentsController.delete_comment(comment_id=comment_id)
        return redirect(reverse_lazy('car_details', kwargs={"car_id": comment.car.id}))
    return redirect('root')