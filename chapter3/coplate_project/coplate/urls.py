from tkinter import N
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
]
