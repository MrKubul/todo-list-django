from django.contrib import admin
from .models import Task
from .models import ToDoList

# Register your models here.

admin.site.register(Task)
admin.site.register(ToDoList)
