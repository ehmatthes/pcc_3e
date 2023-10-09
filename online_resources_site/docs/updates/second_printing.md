---
hide:
  - footer
title: Second Printing
---

# Updates and Errata - Second printing

This page is broken into two parts, Updates and Errata. *Updates* address issues that affect whether your code will run or not. *Errata* refer to minor issues such as typos, and errors in grayed-out code that probably won’t affect the code you’re entering.

Code that produces warnings but still runs correctly is noted under Errata, as this is a fairly common occurrence and the code often still works for a long time while producing warnings.

If you find an error in the book that's not listed here, or can’t get something to work, please let me know. You can reach me through email at ehmatthes@gmail.com, or on Twitter at @ehmatthes.

- [Updates](#updates)
    - [Chapter 16](#chapter-16)
- [Errata](#errata)
    - [Chapter 6](#chapter-6)
    - [Chapter 15](#chapter-15)
    - [Chapter 16](#chapter-16_1)
    - [Chapter 17](#chapter-17)
    - [Chapter 18](#chapter-18)
    - [Chapter 19](#chapter-19)

---

Updates
---

### Chapter 16

On Windows, the calls to `path.read_text()` should all have an `encoding='utf-8'` argument. On page 330, that would look like this:

```python
path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()
```

This also affects the calls to `path.read_text()` on pages 339 and 343. There are a few other grayed-out references to `path.read_text()` that should include this argument, but that shouldn't affect the code you're entering. Those are on pages 332, 334, 336, 339, 345, and 348.

---

Errata
---

### Chapter 6

The output at the bottom of page 95 should say `position`, not `x-position`:

```
Original position: 0
New position: 2
```

### Chapter 15

Matplotlib has a number of predefined styles that you can choose from. The book uses the `seaborn` style, which was base on a style from the [Seaborn](https://seaborn.pydata.org) plotting library. The default style of the Seaborn library has diverged from Matplotlib's `seaborn` style, so they are changing the name of this style to make that clear. (If you're curious to read more about this, see "seaborn styles renamed" in the Matplotlib documentation page [API Changes for 3.6.0](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.0.html#seaborn-styles-renamed).)

If you use `seaborn` as the book does, you'll see a `MatplotlibDeprecationWarning`. This won't prevent your code from running, and it won't affect the style of your output.

To avoid seeing this warning, use `seaborn-v0_8` wherever you see `seaborn` in the book's code. The code should look like this:

```python
plt.style.use('seaborn-v0_8')
```

### Chapter 16

As noted above for Chapter 15, use `seaborn-v0_8` wherever you see `seaborn`.

### Chapter 17

On page 370, the code that starts the `for` loop should go through index `30`, not `5`:

```python
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a new API call for each submission.
    ...
```

### Chapter 18

On page 391, the path to the index.html template should read:

```text
learning_log/learning_logs/templates/learning_logs/index.html
```

### Chapter 19

On page 416, the sentence:

> Make a new *urls.py* file in the directory *ll_project/accounts/* and add the following...

should instead read:

> Make a new *urls.py* file in the directory *learning_log/accounts/* and add the following...

On page 417 under *The login Template* the path to the `accounts/` directory should be `learning_log/accounts/`, not `ll_project/accounts/`. The full path to the `login.html` template should be: `learning_log/accounts/templates/registration/login.html`.

Also on page 417, the word *Settting* should only have two Ts.