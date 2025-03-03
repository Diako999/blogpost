from django.shortcuts import render, redirect
from .models import Blog
from .forms import CreatePost

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
