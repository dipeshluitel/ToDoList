from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import To_do_list
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def active(request):
    return render(request,'active.html')

def save(request):
    return render(request,'info.html')


@login_required
def todo_list(request):
    tasks = To_do_list.objects.filter(user=request.user)
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task= form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('active')
    
    return render(request, 'active.html', {'tasks':tasks, 'form':form})

@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(To_do_list, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('active')

@login_required
def delete_task(request,task_id):
    task=get_object_or_404(To_do_list,id=task_id, user = request.user)
    task.delete()
    return redirect('active')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('active')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html',{'form':form})
