from django.forms import ModelForm
from .models import Todo
from django import forms


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'details', 'priority', 'due_date', 'image']
        widgets = {
            'due_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }