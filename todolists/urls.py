from django.urls import path

from . import views

app_name = 'todolists'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todolist_id>/', views.details, name='details'),
    path('<int:task_id>/complete_task', views.complete_task, name='complete_task'),
    path('<str:chosen_date>/completed_tasks', views.completed_this_day, name='completed_tasks')
]
