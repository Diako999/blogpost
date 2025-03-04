from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer
from .forms import CreatePost

class BlogListView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
class BlogListCreateView():
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
def blogs(request):
    blogs = Blog.objects.all().order_by('-created_at') 
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs/blogs.html', context)

def createPost(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():  # Add parentheses
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')
        else:
            print("Form is invalid")  # Debug line
            print(form.errors)  # Print any form errors
    else:
        form = CreatePost()  # Correct form initialization

    context = {
        'form': form
    }

    return render(request, 'blogs/createBlog.html', context)
