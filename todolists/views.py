from django.shortcuts   import render, get_object_or_404
from django.utils       import timezone
#from django.http        import HttpResponse
#from django.template    import loader

from .models import TodoList, Task


def index(request):
    all_lists = TodoList.objects.order_by('-created_date')
    context = {
        'all_lists' : all_lists,
    }
    return render(request, 'todolists/base.html', context)

def details(request, todolist_id):
    # todolist = TodoList.objects.get(pk=todolist_id)
    todolist = get_object_or_404(TodoList, pk=todolist_id)
    return render(request, 'todolists/details.html', {'todolist':todolist})

def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_completed = False if task.is_completed else True
    task.save()
    print("task saved: "+task.task_text)
    print("task is_completed: "+ str(task.is_completed))
    return index(request)

def completed_this_day(request, chosen_date):
    """Returns the tasks related to the logged user that were completed in the chosen date"""
    if request.user.is_authenticated():
        user_tasks = request.user.created_tasks_set.filter(complete_task=True, completed_date=chosen_date)
        user_tasks += request.user.assigned_tasks_set.filter(complete_task=True, completed_date=chosen_date)
    else:
        # Show some message when the user is not authenticated
        user_tasks = ''
    return render(request, 'todolists/completed_tasks.html', {'user_tasks':user_tasks})