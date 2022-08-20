from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
#     username = models.CharField(max_length=200)

#     def __str__(self):
#         return str(self.username)


class ToDoList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    list_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.list_name)


class Task(models.Model):
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    isFinished = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name) 
