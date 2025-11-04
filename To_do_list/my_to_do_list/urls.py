from django.urls import path
from my_to_do_list import views

urlpatterns = [
    path('',views.todo_list, name='active'),
    path('saved/',views.save, name='save'),
]
