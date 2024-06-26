from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm, LabelForm
from .models import Task, Label


@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.user, request.POST)
        if form.is_valid():
            task = form.save(False)
            task.owner = request.user
            task.save()
            form.save_m2m()
            return redirect('task_list')
    else:
        form = TaskForm(request.user)
    user_labels = Label.objects.filter(owner=request.user)
    print(user_labels)
    return render(request, 'tasks/task_form.html',
                  {'form': form, 'user_labels': user_labels}
                  )


@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.owner != request.user:
        return redirect('task_list')

    if request.method == 'POST':
        form = TaskForm(request.user, request.POST, instance=task)
        if form.is_valid():
            task = form.save(False)
            if 'completion_status' in form.cleaned_data:
                task.completion_status = form.cleaned_data['completion_status']
            task.save()
            form.save_m2m()
            return redirect('task_list')
    else:
        form = TaskForm(request.user, instance=task)
    user_labels = Label.objects.filter(owner=request.user)
    return render(request, 'tasks/task_form.html',
                  {'form': form, 'user_labels': user_labels, 'task': task})


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


@login_required
def label_list(request):
    labels = Label.objects.filter(owner=request.user)
    return render(request, 'tasks/label_list.html', {'labels': labels})


@login_required
def create_label(request):
    if request.method == 'POST':
        form = LabelForm(request.user, request.POST)
        if form.is_valid():
            label = form.save(commit=False)
            label.owner = request.user
            label.save()
        return redirect('label_list')
    else:
        form = LabelForm(request.user)
    return render(request, 'tasks/label_form.html', {'form': form})


@login_required
def update_label(request, pk):
    label = get_object_or_404(Label, pk=pk)
    if label.owner != request.user:
        return redirect('label_list')
    if request.method == 'POST':
        form = LabelForm(request.user, request.POST, instance=label)
        if form.is_valid():
            label = form.save(False)
            label.owner = request.user
            label.save()
            return redirect('label_list')
    else:
        form = LabelForm(request.user, instance=label)
    return render(request, 'tasks/label_form.html', {'form': form})


@login_required
def delete_label(request, pk):
    label = get_object_or_404(Label, pk=pk)
    if label.owner != request.user:
        return redirect('label_list')
    if request.method == 'POST':
        label.delete()
        return redirect('label_list')
    else:
        return render(request, 'tasks/label_confirm_delete.html',
                      {'label': label}
                      )
