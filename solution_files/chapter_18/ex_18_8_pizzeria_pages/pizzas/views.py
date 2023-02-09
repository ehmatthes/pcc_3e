from django.shortcuts import render

from .models import Pizza

def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Page showing all pizzas that are available."""
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)