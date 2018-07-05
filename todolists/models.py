"""Models used by the todolists app"""
#import datetime

from django.db import models
#from django.utils import timezone

# Create your models here.

class TodoList(models.Model):
    """Defines the attributes of a TODO list"""
    list_title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.list_title
    """def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)"""

class Task(models.Model):
    """Defines the attributes of a task from a todo list"""
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField('Due Date', blank=True, null=True)
    # include here a variable for related users later
    def __str__(self):
        return self.task_text
