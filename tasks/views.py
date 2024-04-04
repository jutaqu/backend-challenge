from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task


@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.user, request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(request.user)
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.owner != request.user:
        return redirect('task_list')

    if request.method == 'POST':
        form = TaskForm(request.user, request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            if 'completion_status' in form.cleaned_data:
                task.completion_status = form.cleaned_data['completion_status']
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(request.user, instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.owner != request.user:
        return redirect('task_list')
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    else:
        return render(request, 'tasks/task_confirm_delete.html',
                      {'task': task}
                      )
