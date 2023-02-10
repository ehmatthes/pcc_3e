from django.shortcuts import render


def index(request):
    """The home page for Blog."""
    return render(request, 'blogs/index.html')
