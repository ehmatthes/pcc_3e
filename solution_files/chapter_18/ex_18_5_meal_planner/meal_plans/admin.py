from django.contrib import admin

from .models import Meal, MealItem

admin.site.register(Meal)
admin.site.register(MealItem)