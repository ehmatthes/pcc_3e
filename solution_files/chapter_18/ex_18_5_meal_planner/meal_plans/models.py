from django.db import models

class Meal(models.Model):
    """An model for a single meal."""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the meal."""
        return self.name

class MealItem(models.Model):
    """An indidivual part of a meal."""
    name = models.CharField(max_length=200)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the item."""
        return self.name 
