from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('register/', include('user.urls')),
     path('login/', include('user.urls'), name='login'),
    path('blogs/', include('blogs.urls')),
]
