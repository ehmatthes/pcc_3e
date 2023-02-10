from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    """Represents one person or organization's blog."""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the blog."""
        return self.name

class BlogPost(models.Model):
    """Represents an individual post."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=500)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representing the blog post."""
        if len(self.title) > 50:
            return f"{self.title[:50]}..."
        else:
            return self.title