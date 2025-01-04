from django import forms

from .models import Car, Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content', 'parent']

        widgets = {
            'content' : forms.Textarea(),
        }