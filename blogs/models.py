from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(max_length= 400, null=False)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title