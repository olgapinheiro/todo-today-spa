import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class TodoList(models.Model):
    list_title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.list_title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Task(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=200)
    isCompleted = models.BooleanField(default='false')
    due_date = models.DateField('Due Date')
    # include here a variable for related users later
    def __str__(self):
        return self.task_text
