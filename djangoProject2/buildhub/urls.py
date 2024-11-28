from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('buildhub/', views.blog, name='blog'),
    path('AddBlog/', views.add_blog, name='addblog'),

]