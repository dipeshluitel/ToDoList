from django.shortcuts import render

# Create your views here.
def active(request):
    return render(request,'active.html')