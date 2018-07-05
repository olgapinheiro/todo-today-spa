from django.db import models

# Create your models here.

class TodoList(models.Model):
    list_title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

class Task(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=200)
    isCompleted = models.BooleanField(default='false')
    deadline = models.DateField('deadline date')
    # include here a variable for related users later