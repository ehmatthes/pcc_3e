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
    - [Chapter 6](#chapter-6)
    - [Chapter 9](#chapter-9)
    - [Chapter 10](#chapter-10)
    - [Chapter 15](#chapter-15)
    - [Chapter 16](#chapter-16)
    - [Chapter 18](#chapter-18)
    - [Chapter 19](#chapter-19)

---

Updates
---

There are no updates to note at this time.

---

Errata
---

### Chapter 6

The output at the bottom of page 95 should say `position`, not `x-position`:

```
Original position: 0
New position: 2
```


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

### Chapter 15

Matplotlib has a number of predefined styles that you can choose from. The book uses the `seaborn` style, which was base on a style from the [Seaborn](https://seaborn.pydata.org) plotting library. The default style of the Seaborn library has diverged from Matplotlib's `seaborn` style, so they are changing the name of this style to make that clear. (If you're curious to read more about this, see "seaborn styles renamed" in the Matplotlib documentation page [API Changes for 3.6.0](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#seaborn-styles-renamed).)

If you use `seaborn` as the book does, you'll see a `MatplotlibDeprecationWarning`. This won't prevent your code from running, and it won't affect the style of your output.

To avoid seeing this warning, use `seaborn-v0_8` wherever you see `seaborn` in the book's code. The code should look like this:

```python
plt.style.use('seaborn-v0_8')
```

### Chapter 16,

As noted above for Chapter 15, use `seaborn-v0_8` wherever you see `seaborn`.

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

On page 416, the sentence 

> Make a new *urls.py* file in the directory *ll_project/accounts/* and add the following...

should instead read:

> Make a new *urls.py* file in the directory *learning_log/accounts/* and add the following...

On page 425, in the grayed out code for *models.py*, the `text` attribute should be lowercase:

```python
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    ...
```