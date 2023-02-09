from django.shortcuts import render

from .models import Meal

def index(request):
    """The home page for Meal Planner."""
    return render(request, 'meal_plans/index.html')

def meals(request):
    """Page to show all available meals."""
    meals = Meal.objects.all()
    context = {'meals': meals}
    return render(request, 'meal_plans/meals.html', context)

def meal(request, meal_id):
    """Page to show an individual meal."""
    meal = Meal.objects.get(id=meal_id)
    meal_items = meal.mealitem_set.all()

    context = {'meal': meal, 'meal_items': meal_items}
    return render(request, 'meal_plans/meal.html', context)