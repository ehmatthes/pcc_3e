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