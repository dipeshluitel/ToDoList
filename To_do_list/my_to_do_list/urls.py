from django.urls import path
from my_to_do_list import views

urlpatterns = [
    path('',views.active, name='active')
]
