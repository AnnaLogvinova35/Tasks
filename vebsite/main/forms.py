from .models import Task
from django.forms import ModelForm, widgets, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "deadline"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
                   "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
                   "deadline": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите срок выполнения'})
                   }