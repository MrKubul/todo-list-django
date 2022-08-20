from django.shortcuts import render
from .models import User, Task, ToDoList

def home(request):
    users = User.objects.all()
    tasks = Task.objects.all()
    todo_lists = ToDoList.objects.all()
    context = {
        "users": users,
        "tasks": tasks,
        "todo_lists": todo_lists
    }
    return render(request, 'home.html', context)

def test(request):
    return render(request, 'main.html')
