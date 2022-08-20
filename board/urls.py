from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('', views.home, name="home"),
    path('list-view/', views.list_view, name = "list-view"),
    path('create-list/', views.create_list, name = "create-list"),
    path('update-list/<str:pk>', views.update_list, name = "update-list"),
    path('add-task/', views.add_task, name = "add-task"),
    path('update-task/<str:pk>', views.update_task, name = "update-task"),
    path('delete-task/<str:pk>', views.delete_task, name = "delete-task"),
] 