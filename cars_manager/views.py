from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView, 
                                  DetailView, 
                                  FormView, 
                                  DeleteView)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import CommentForm, CarForm
from .models import Car, Comments
from .service import CarController, CommentsController


class CarsMainPage(ListView):
    template_name = "cars_manager/main_page.html"
    model = Car
    context_object_name = 'cars'
    extra_context = {'title': 'Авто-мир'}
    
class CarsCreateFormView(CreateView):
    template_name = 'cars_manager/base_form.html'
    form_class = CarForm
    extra_context = {'title': 'Поделитесь мнением об автомобиле!', 'action': 'Создать'}

    def form_valid(self, form):
        new_car = form.save()
        new_car.owner = self.request.user
        new_car.save()
        return super().form_valid(form)

class CarsUpdateFormView(UpdateView):
    template_name = 'cars_manager/base_form.html'
    form_class = CarForm
    extra_context = {'title': 'Поделитесь мнением об автомобиле!', 'action': 'Обновить'}

class CarsDetailsView(DetailView):
    template_name = "cars_manager/car_details.html"
    model = Car
    context_object_name = 'car'
    pk_url_kwarg = 'car_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_comment_form'] = CommentForm()
        return context
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentForm

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')

    def form_valid(self, form):
        car = get_object_or_404(Car, id=self.kwargs.get('car_id'))

        content = form.cleaned_data.get('content')
        parent = form.cleaned_data.get('parent')

        CommentsController.create_comment(content=content,
                                            author_id=self.request.user.id,
                                            car=car,
                                            reply_to=parent)
        
        return redirect(self.get_success_url())

class CarsDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy('root')
    template_name = "cars_manager/base_delete.html"
    pk_url_kwarg = 'car_id'

@login_required
def delete_comment(request, comment_id):
    comment = CommentsController.get_comment(id=comment_id)
    if comment:
        CommentsController.delete_comment(comment_id=comment_id)
        return redirect(reverse_lazy('car_details', kwargs={"car_id": comment.car.id}))
    return redirect('root')