from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import To_do_list

# Create your views here.
def active(request):
    return render(request,'active.html')

def save(request):
    return render(request,'save.html')

def todo_list(request):
    tasks = To_do_list.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('active')
    
    return render(request, 'active.html', {'tasks':tasks, 'form':form})

def toggle_task(request, task_id):
    task = get_object_or_404(To_do_list, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('active')