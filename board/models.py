from django.db import models
from django.contrib.auth.models import User

class ToDoList(models.Model):
    list_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    list_name = models.CharField(max_length=200) ## user cant have two lists named the same
    created_time = models.DateTimeField(auto_now=True)
    due_date = models.DateField()

    def __str__(self):
        return str(self.list_name)


class Task(models.Model):
    parent_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    task_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now=True)
    isFinished = models.BooleanField(default=False)
    due_date = models.DateTimeField()

    def __str__(self):
        return str(self.name) 
