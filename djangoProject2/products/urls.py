from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from .import views

urlpatterns = [
path('cpu/', views.cpu, name='cpu'),
path('mobo/', views.mobo, name='mobo'),
]