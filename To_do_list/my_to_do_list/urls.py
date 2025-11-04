from django.urls import path
from my_to_do_list import views

urlpatterns = [
    path('',views.todo_list, name='active'),
    path('toggle/<int:task_id>', views.toggle_task,name="toggle_task"),
    path('delete/<int:task_id>', views.delete_task,name="delete_task"),
    path('saved/',views.save, name='save'),
]
