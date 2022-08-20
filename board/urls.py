from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('list-view/', views.list_view, name = "list-view"),
    path('create-list/', views.create_list, name = "create-list"),
    path('add-task/', views.add_task, name = "add-task"),
] 