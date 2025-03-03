from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', register, name='register'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]