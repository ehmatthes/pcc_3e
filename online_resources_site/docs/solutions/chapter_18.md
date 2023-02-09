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