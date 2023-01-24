---
hide:
  - footer
title: First Printing
---

# Updates and Errata - First printing

This page is broken into two parts, Updates and Errata. *Updates* address issues that affect whether your code will run or not. *Errata* refer to minor issues such as typos, and errors in grayed-out code that probably won’t affect the code you’re entering.

Code that produces warnings but still runs correctly is noted under Errata, as this is a fairly common occurrence and the code often still works for a long time while producing warnings.

If you find an error in the book that's not listed here, or can’t get something to work, please let me know. You can reach me through email at ehmatthes@gmail.com, or on Twitter at @ehmatthes.

- [Updates](#updates)
- [Errata](#errata)
    - [Chapter 9](#chapter-9)
    - [Chapter 10](#chapter-10)
    - [Chapter 18](#chapter-18)
    - [Chapter 19](#chapter-19)




Updates
---

There are no updates to note at this time.

---

Errata
---

### Chapter 9

On page 167, the docstring for the `__init__()` method in *electric_car.py* should have triple quotes on both ends:

```python
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        ...
```

### Chapter 10

On page 200, Exercise 10-7 should read "Wrap your code from Exercise 10-6 in a while loop..."

Also, Exercise 10-9 should refer to Exercise 10-8.

### Chapter 18

On page 399, the listing for *topics.html* has an extra closing tag `</li>`. It should look like this:

```html
    {% for topic in topics %}
      <li>
        <a href="{% url 'learning_logs:topic' topic.id %}">
          {{ topic.text }}</a>
      </li>
      ...
```

### Chapter 19

On page 425, in the grayed out code for *models.py*, the `text` attribute should be lowercase:

```python
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    ...
```