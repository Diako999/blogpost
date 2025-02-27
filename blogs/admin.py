from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Fields displayed in the list view
    search_fields = ('title', 'author')  # Search functionality
    list_filter = ('created_at',)  # Filter by date
