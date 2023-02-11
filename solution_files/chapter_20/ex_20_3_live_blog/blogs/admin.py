from django.contrib import admin

from .models import Blog, BlogPost

admin.site.register(Blog)
admin.site.register(BlogPost)