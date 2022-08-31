from django import forms
from django.forms import ModelForm
from .models import ToDoList, Task

class ListForm(ModelForm):
    class Meta:
        model = ToDoList
        exclude = ['list_owner']
        widgets = {
            'due_date': forms.TextInput(attrs={'placeholder': 'month/day/year (numerically)'})
        }

class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ['task_owner', 'parent_list'] 
        widgets = {
            'due_date': forms.TextInput(attrs={'placeholder': 'month/day/year (numerically)'}),
            'description': forms.Textarea(attrs={'rows': 2})

        }
