from django.shortcuts   import render, get_object_or_404
#from django.http        import HttpResponse
#from django.template    import loader

from .models import TodoList, Task


def index(request):
    all_lists = TodoList.objects.order_by('-pub_date')
    context = {
        'all_lists' : all_lists,
    }
    return render(request, 'todolists/index.html', context)

def details(request, todolist_id):
    # todolist = TodoList.objects.get(pk=todolist_id)
    todolist = get_object_or_404(TodoList, pk=todolist_id)
    return render(request, 'todolists/details.html', {'todolist':todolist})

def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_completed = False if task.isCompleted else True
    task.save()