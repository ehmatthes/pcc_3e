from django import forms

from .models import Blog, BlogPost


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body']

        widgets = {'body': forms.Textarea(attrs={'cols': 80})}