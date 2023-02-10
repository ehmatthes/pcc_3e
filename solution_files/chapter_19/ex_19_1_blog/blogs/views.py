from django.shortcuts import render

from .models import Blog, BlogPost


def index(request):
    """The home page for Blog."""
    return render(request, 'blogs/index.html')

def blogs(request):
    """Page to view all blogs that have been created."""
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """Page to view an individual blog, and all its posts."""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.blogpost_set.all()

    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)