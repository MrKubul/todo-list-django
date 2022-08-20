from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User, Task, ToDoList
from .forms import ListForm, TaskForm
from django.shortcuts import redirect

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exists')

        user.authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password doesnt exist')

    context = {}
    return(request, 'login_and_registration.html', context)


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
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-view')


    form = ListForm()
    context = {"form": form}
    return render(request, 'create_list_form.html', context)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-view')
    form = TaskForm()
    context = {"form": form}
    return render(request, 'create_task_form.html', context)

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if form.is_valid():
            form.save()
            return redirect('list-view')
    context = {"form": form}
    return render(request, 'create_task_form.html', context)

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('list-view')
    return render(request, 'delete_task_form.html')
