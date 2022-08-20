from django.forms import ModelForm
from .models import ToDoList, Task

class ListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = '__all__'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__' 