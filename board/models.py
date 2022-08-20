from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)

    def __str__(self):
        return str(self.username)


class ToDoList(models.Model):
    list_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.list_name)


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) 
