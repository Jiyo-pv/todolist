from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Display tasks
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')

    return render(request, 'index.html', {'tasks': tasks, 'form': form})


# Toggle complete
def toggle_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = not task.completed
    task.save()
    return redirect('list')


# Delete task
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('list')