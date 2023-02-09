from django.shortcuts import render

def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzas/index.html')
