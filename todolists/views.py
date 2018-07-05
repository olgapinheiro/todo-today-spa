from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import TodoList, Task


def index(request):
    all_lists = TodoList.objects.order_by('-pub_date')
    template = loader.get_template('todolists/index.html')
    context = {
        'all_lists' : all_lists,
    }
    return render(request,'todolists/index.html',context)