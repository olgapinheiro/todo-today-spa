from django.urls import path

from . import views

app_name = 'todolists'
urlpatterns = [
    path('', views.base, name='base'),
    path(r'^<int:todolist_id>/$', views.details, name='details'),
    path(r'^complete_task/$', views.complete_task, name='complete_task'),
    path(r'^<str:chosen_date>/completed_tasks/$', views.completed_this_day, name='completed_tasks'),
    path(r'^test.html', views.test, name="test"),
    path(r'add_task/', views.add_task, name='add_task'),
]
