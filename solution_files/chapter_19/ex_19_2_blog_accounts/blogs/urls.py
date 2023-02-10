"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page to view all blogs that have been created.
    path('blogs/', views.blogs, name='blogs'),
    # Page to view an individual blog, and all its posts.
    path('blog/<int:blog_id>/', views.blog, name='blog'),

    # Page for creating a new blog.
    path('new_blog/', views.new_blog, name='new_blog'),
    # Page for writing a new post.
    path('new_post/<int:blog_id>/', views.new_post, name='new_post'),
    # Page for editing an existing post.
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]