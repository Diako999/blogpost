from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', register, name='register'),
    path('login/', LoginView.as_view(), name = 'login')
]