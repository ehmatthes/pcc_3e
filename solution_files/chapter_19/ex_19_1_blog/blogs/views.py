from django.shortcuts import render, redirect

from .models import Blog, BlogPost
from .forms import BlogForm, BlogPostForm


def index(request):
    """The home page for Blog."""
    return render(request, 'blogs/index.html')

def blogs(request):
    """Page to view all blogs that have been newd."""
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """Page to view an individual blog, and all its posts."""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.blogpost_set.all()

    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)

def new_blog(request):
    """Page to new a new blog."""
    if request.method != 'POST':
        # No data submitted; new a blank form.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

def new_post(request, blog_id):
    """Page to create a new post."""
    blog = Blog.objects.get(id=blog_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blogs:blog', blog_id=blog_id)

    # Display a blank or invalid form.
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
    """Page to edit an existing post."""
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = BlogPostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)

    context = {'post': post, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
