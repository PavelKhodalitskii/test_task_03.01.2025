from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView, 
                                  DetailView,                                   
                                  DeleteView)

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

from .forms import CommentForm, CarForm
from .models import Car
from .service import CommentsController


class CarsMainPage(ListView):
    template_name = "cars_manager/main_page.html"
    model = Car
    context_object_name = 'cars'
    extra_context = {'title': 'Авто-мир'}
    
class CarsCreateFormView(PermissionRequiredMixin, CreateView):
    template_name = 'cars_manager/base_form.html'
    form_class = CarForm
    extra_context = {'title': 'Поделитесь мнением об автомобиле!', 'action': 'Создать'}
    # Только пользователи, у котрых есть разрешение на добавление автомобилей могут их добавлять
    permission_required = 'cars_manager.add_car'

    def form_valid(self, form):
        new_car = form.save()
        new_car.owner = self.request.user
        new_car.save()
        return super().form_valid(form)

class CarsUpdateFormView(PermissionRequiredMixin, UpdateView):
    template_name = 'cars_manager/base_form.html'
    form_class = CarForm
    model = Car
    pk_url_kwarg = 'car_id'
    extra_context = {'title': 'Поделитесь мнением об автомобиле!', 'action': 'Обновить'}
    permission_required = 'cars_manager.change_car'
    

class CarsDetailsView(DetailView):
    template_name = "cars_manager/car_details.html"
    model = Car
    context_object_name = 'car'
    pk_url_kwarg = 'car_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{context['car'].make} {context['car'].model}"
        context['create_comment_form'] = CommentForm()
        return context
    
class CommentCreateView(PermissionRequiredMixin, CreateView):
    form_class = CommentForm
    permission_required = 'cars_manager.add_comments'

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')

    def form_valid(self, form):
        car = get_object_or_404(Car, id=self.kwargs.get('car_id'))

        content = form.cleaned_data.get('content')
        parent = form.cleaned_data.get('parent')

        # Создание комментария
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

@permission_required('cars_manager.delete_comment')
def delete_comment(request, comment_id):
    comment = CommentsController.get_comment(id=comment_id)
    if comment:
        # Пользователь может удалять только свои комментарии
        if comment.author.id == request.user.id:
            CommentsController.delete_comment(comment_id=comment_id)
        return redirect(reverse_lazy('car_details', kwargs={"car_id": comment.car.id}))
    return redirect('root')