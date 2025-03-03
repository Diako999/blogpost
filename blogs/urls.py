from django.contrib import admin
from django.urls import path
from .views import blogs, createPost
urlpatterns = [
    path('', blogs, name='blogs'),
    path('create/', createPost, name='create'),
]
