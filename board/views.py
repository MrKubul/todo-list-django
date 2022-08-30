from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import User, Task, ToDoList
from .forms import ListForm, TaskForm
from django.shortcuts import redirect

def login_page(request):
    page = 'login'

    if request.method == 'POST':
        _username = request.POST.get('username')
        _password = request.POST.get('password')

        try:
            user = User.objects.get(username=_username)
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
            messages.error(request, "Something went wrong!")

    context = {"form": form}
    return render(request, 'login_and_registration.html', context)

def home(request):
    if request.method == 'POST':  
        list = ToDoList(list_owner=request.user)
        try:
            all_user_lists = ToDoList.objects.get(list_owner=request.user)
            all_used_list_names = [list.list_name for list in all_user_lists]
            form = ListForm(request.POST, instance=list)
            if request.POST.get('list_name') not in all_used_list_names:
                if form.is_valid():
                    form.save()
                    messages.success(request, "List created sucessfuly")
            else:
                messages.error(request, "List name already used!")
            return redirect('home')
        except ObjectDoesNotExist:
            pass

    form = ListForm()
    context = {"form": form}
    return render(request, 'home.html', context)

def list_view(request):
    if request.method == 'POST':
        try:
            list_name = request.POST.get('list_name')
            list = ToDoList.objects.get(list_name = list_name)
            all_prev_taks = Task.objects.get(parent_list = list_name)
            all_task_names = [task.name for task in all_prev_taks]
            if request.POST.get('name') not in all_task_names:
                task = Task(task_owner=request.user, list=list)
                form = TaskForm(request.POST, instance=task)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Task added succesfuly")
                    return redirect('list-view')
                else:
                    messages.error(request, "Error happend while adding task!")
            else:
                messages.error(request, "task with that name already exists")
        except ObjectDoesNotExist:
            pass

    tasks = []
    todo_lists = []
    try:
        tasks = Task.objects.get(task_owner = request.user)
        todo_lists = ToDoList.objects.get(list_owner = request.user)
        print("DLUGOSC TO ", len(todo_lists))
    except ObjectDoesNotExist:
            pass

    print("DLUGOSC TO ", len(todo_lists))

    form = TaskForm()
    context = {"form": form,
                "tasks": tasks,
                "todo_lists": todo_lists
    }

    return render(request, 'list_view.html', context)

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

def delete_list(request, pk):
    list = ToDoList.objects.get(id=pk)
    if request.method == 'POST':
        list.delete()
        return redirect('list-view')
    return render(request, 'delete_list_form.html')

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
