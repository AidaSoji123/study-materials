from django.shortcuts import render, redirect
from .models import TodoItem

def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        new_todo = TodoItem(title=title)
        new_todo.save()
        return redirect('index')

def complete_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def delete_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
