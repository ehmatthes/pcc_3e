"""Defines URL patterns for pizzas."""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Page showing all pizzas.
    path('pizzas/', views.pizzas, name='pizzas'),
    # Page showing an individual pizza.
    path('pizza/<int:pizza_id>/', views.pizza, name='pizza'),
]