from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from .models import Blog
from .serializers import BlogSerializer
from .forms import CreatePost

# ✅ Protect API: Only authenticated users can access
class BlogListCreateView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]  

class BlogListView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

# ✅ Protect Template Views
@login_required
def blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blogs/blogs.html', {'blogs': blogs})

@login_required
def createPost(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')
    else:
        form = CreatePost()

    return render(request, 'blogs/createBlog.html', {'form': form})
