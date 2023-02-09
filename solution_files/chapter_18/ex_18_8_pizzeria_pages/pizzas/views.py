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

def pizza(request, pizza_id):
    """Page showing information about an individual pizza."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()

    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)