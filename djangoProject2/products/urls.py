from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from .import views

urlpatterns = [
path('cpu/', views.cpu, name='cpu'),
path('mobo/', views.mobo, name='mobo'),
path('cpucooler/', views.cpucooler, name='cpucooler'),
path('ram/', views.ram, name='ram'),
path('storage/', views.storage, name='storage'),
path('gpu/', views.gpu, name='gpu'),
path('psu/', views.psu, name='psu'),
path('case/', views.case, name='case'),
]