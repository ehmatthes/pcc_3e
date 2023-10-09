---
hide:
  - footer
title: Third Printing
---

# Updates and Errata - Third printing

This page is broken into two parts, Updates and Errata. *Updates* address issues that affect whether your code will run or not. *Errata* refer to minor issues such as typos, and errors in grayed-out code that probably won’t affect the code you’re entering.

Code that produces warnings but still runs correctly is noted under Errata, as this is a fairly common occurrence and the code often still works for a long time while producing warnings.

If you find an error in the book that's not listed here, or can’t get something to work, please let me know. You can reach me through email at ehmatthes@gmail.com, or on Twitter at @ehmatthes.

- [Updates](#updates)
- [Errata](#errata)
    - [Chapter 17](#chapter-17)
    - [Chapter 18](#chapter-18)
    - [Chapter 19](#chapter-19)

---

Updates
---

There are no updates to note at this time.

---

Errata
---

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

On page 417 under *The login Template* the path to the `accounts/` directory should be `learning_log/accounts/`, not `ll_project/accounts/`. The full path to the `login.html` template should be: `learning_log/accounts/templates/registration/login.html`.

Also on page 417, the word *Settting* should only have two Ts.

