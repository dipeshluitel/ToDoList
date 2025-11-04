from django.shortcuts import render

# Create your views here.
def active(request):
    return render(request,'active.html')

def save(request):
    return render(request,'save.html')