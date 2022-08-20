from django.shortcuts import render
from .models import User, Task, ToDoList

def home(request):
    return render(request, 'home.html')

def list_view(request):
    users = User.objects.all()
    tasks = Task.objects.all()
    todo_lists = ToDoList.objects.all()
    context = {
        "users": users,
        "tasks": tasks,
        "todo_lists": todo_lists
    }
    return render(request, 'list_view.html', context)

def create_list(request):
    return render(request, 'crear_list_form.html')

def add_task(request):
    return render(request, 'create_task_form.html')
