from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.todo_list, name='todo_create'),
]