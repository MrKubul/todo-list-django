from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('', views.home, name="home"),
    path('list-view/', views.list_view, name = "list-view"),
    path('update-list/<str:pk>', views.update_list, name = "update-list"),
    path('delete-list/<str:pk>', views.delete_list, name = "delete-task"),
    path('update-task/<str:pk>', views.update_task, name = "update-task"),
    path('delete-task/<str:pk>', views.delete_task, name = "delete-task"),
] 