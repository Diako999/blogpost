from django.contrib import admin
from django.urls import path
from .views import blogs, createPost, BlogListView, BlogListCreateView
urlpatterns = [
    path('', blogs, name='blogs'),
    path('create/', createPost, name='create'),
    path('api/', BlogListView.as_view(), name='api'),
]
