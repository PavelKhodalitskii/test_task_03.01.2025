from django import forms

from .models import Car, Comments


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'description']

        widgets = {
            'year' : forms.IntegerField(min_value=1885, max_value=3000),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content', 'parent']

        widgets = {
            'content' : forms.Textarea(),
        }