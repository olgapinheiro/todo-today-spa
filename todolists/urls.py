from django.urls import path

from . import views

app_name = 'todolists'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todolist_id>/', views.details, name='details'),
    path('<int:todolist_id>/complete_task', views.complete_task, name='complete_task')
]
