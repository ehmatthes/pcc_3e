---
hide:
  - footer
title: "Solutions: Chapter 18"
---

# Solutions - Chapter 18

---

## 18-1: New Projects

To get a better idea of what Django does, build a couple empty projects and look at what Django creates. Make a new folder with a simple name, like *tik_gram* or *insta_tok* (outside of your *learning_log* directory), navigate to that folder in a terminal, and create a virtual environment. Install Django and run the command `django-admin startproject tg_project .` (making sure to include the dot at the end of the command).

Look at the files and folders this command creates, and compare them to Learning Log. Do this a few times, until you’re familiar with what Django creates when starting a new project. Then delete the project directories if you wish.

***Note:** Early printings of the third edition mention the commmand `django-admin.py startproject`. That was a holdover from earlier editions; you should use the command `django-admin startproject` (without the `.py`), as shown in the main part of the text.*

You should see output similar to the following:

```
(tg_env)tik_gram$ django-admin startproject tg_project .
(tg_env)tik_gram$ ls
manage.py   tg_project
(tg_env)tik_gram$ ls tg_project 
__init__.py asgi.py     settings.py urls.py     wsgi.py
```

## 18-2: Short Entries

The `__str__()` method in the `Entry` model currently appends an ellipsis to every instance of `Entry` when Django shows it in the admin site or the shell. Add an `if` statement to the `__str__()` method that adds an ellipsis only if the entry is longer than 50 characters. Use the admin site to add an entry that’s fewer than 50 characters in length, and check that it doesn’t have an ellipsis when viewed.

```python title="models.py"
from django.db import models

class Topic(models.Model):
    ...

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text
```

## 18-4: Pizzeria

Start a new project called `pizzeria_project` with an app called `pizzas`. Define a model `Pizza` with a field called `name`, which will hold name values, such as `Hawaiian` and `Meat Lovers`. Define a model called `Topping` with fields called `pizza` and `name`. The `pizza` field should be a foreign key to `Pizza`, and `name` should be able to hold values such as `pineapple`, `Canadian bacon`, and `sausage`.

Register both models with the admin site, and use the site to enter some pizza names and toppings. Use the shell to explore the data you entered.

*An entire Django project, even a small one, is too much to list here. You can see the full solution to this project [here](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_18/ex_18_4_pizzeria).*

## 18-5: Meal Planner

Consider an app that helps people plan their meals throughout the week. Make a new folder called *meal_planner*, and start a new Django project inside this folder. Then make a new app called `meal_plans`. Make a simple home page for this project.

*The full solution is [here](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_18/ex_18_5_meal_planner).*

## 18-6: Pizzeria Home Page

Add a home page to the `Pizzeria` project you started in Exercise 18-4 (page 388).

*The full solution is [here](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_18/ex_18_6_pizzeria_home_page).*

## 18-8: Pizzeria Pages

Add a page to the `Pizzeria` project from Exercise 18-6 (page 392) that shows the names of available pizzas. Then link each pizza name to a page displaying the pizza’s toppings. Make sure you use template inheritance to build your pages efficiently.

*The full solution is [here](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_18/ex_18_8_pizzeria_pages).*