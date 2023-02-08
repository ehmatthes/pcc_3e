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
    - [Chapter 12](#chapter-12-temporary-update)
- [Errata](#errata)
    - [Chapter 6](#chapter-6)
    - [Chapter 15](#chapter-15)
    - [Chapter 16](#chapter-16)


Updates
---

### Chapter 12 (temporary update)

If you try to install Pygame using the book's instructions, and you're using Python 3.11, you'll get an error similar to the following:

```
$ python -m pip install pygame 
Collecting pygame
  Using cached pygame-2.1.2.tar.gz (10.1 MB)
  Preparing metadata (setup.py) ... done
Installing collected packages: pygame
  DEPRECATION: pygame is being installed using the legacy 'setup.py...
  Running setup.py install for pygame ... error
  error: subprocess-exited-with-error
  ...
error: legacy-install-failure
...
```

There is a pre-release version of Pygame that works on Python 3.11. To install a working version, use the following command instead:

```
$ pip install --pre pygame
Collecting pygame
  Downloading pygame-2.1.3.dev8...
     ━━━━━━ 12.9/12.9 MB 6.3 MB/s eta 0:00:00
Installing collected packages: pygame
Successfully installed pygame-2.1.3.dev8
```

A new release should be made shortly. As soon as [this issue](https://github.com/pygame/pygame/issues/3522) is closed, this workaround will no longer be needed.

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