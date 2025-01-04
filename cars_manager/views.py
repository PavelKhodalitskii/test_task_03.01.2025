from django.shortcuts import redirect, render

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, DeleteView

from .forms import CommentForm
from .models import Car, Comments
from .service import CarController, CommentsController

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

def delete_comment(request, comment_id):
    comment = CommentsController.get_comment(id=comment_id)
    if comment:
        CommentsController.delete_comment(comment_id=comment_id)
        return redirect(reverse_lazy('car_details', kwargs={"car_id": comment.car.id}))
    return redirect('root')

# class 

class TestView(TemplateView):
    template_name = "cars_manager/base.html"