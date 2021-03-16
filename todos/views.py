from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, UpdateTaskForm

# Create your views here.


def index(request):
    todos = Task.objects.all()
    count_todos = todos.count()

    completed_todo = Task.objects.filter(complete=True)
    count_completed_todo = completed_todo.count()

    uncompleted = count_todos - count_completed_todo

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    context = {
        'todos': todos,
        'form': form,
        'count_todos': count_todos,
        'count_completed_todo': count_completed_todo,
        'uncompleted': uncompleted,
    }
    return render(request, 'todos/index.html', context)


def update(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateTaskForm(instance=task)
    context = {
        'form': form
    }
    return render(request, 'todos/update_task.html', context)


def delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'todos/delete_task.html')
