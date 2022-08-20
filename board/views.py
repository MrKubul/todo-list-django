from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import User, Task, ToDoList
from .forms import ListForm, TaskForm
from django.shortcuts import redirect

def login_page(request):
    page = 'login'

    if request.method == 'POST':
        _username = request.POST.get('username')
        _password = request.POST.get('password')

        try:
            user = User.objects.get(username = _username)
        except:
            messages.error(request, 'User does not exists')

        user = authenticate(request, username=_username, password=_password)
        if user is not None:
            user.username = user.username.lower()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password doesnt exist')

    context = {"page": page}
    return render(request, 'login_and_registration.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "sth went wrong")

    context = {"form": form}
    return render(request, 'login_and_registration.html', context)

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

def update_list(request, pk):
    listToUpdate = ToDoList.objects.get(id=pk)
    form = ListForm(instance = listToUpdate)

    if request.method == 'POST':
        form = ListForm(request.POST, instance=listToUpdate)
        if form.is_valid():
            form.save()
            return redirect('list-view')
    context = {"form": form}
    return render(request, 'create_list_form.html', context)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-view')
        else:
            messages.error(request, "nie towja tablica, zostaw!!!")
    form = TaskForm()
    context = {"form": form}
    return render(request, 'create_task_form.html', context)

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
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
