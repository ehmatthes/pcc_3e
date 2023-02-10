---
hide:
  - footer
title: "Solutions: Chapter 19"
---

# Solutions - Chapter 19

---

## 19-1: Blog

Start a new Django project called `Blog`. Create an app called `blogs`, with one model that represents an overall blog, and one model that represents an individual blog post. Give each model an appropriate set of fields. Create a superuser for the project, and use the admin site to make a blog and a couple of short posts. Make a home page that shows all posts in an appropriate order.

Create pages for making a blog, for making new posts, and for editing existing posts. Use your pages to make sure they work.

*The full solution is [here](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_19/ex_19_1_blog).*

## 19-2: Blog Accounts

Add a user authentication and registration system to the `Blog` project you started in Exercise 19-1 (page 415). Make sure logged-in users see their username somewhere on the screen and unregistered users see a link to the registration page.

*The full solution is [here](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_19/ex_19_2_blog_accounts).*

## 19-3: Refactoring

There are two places in *views.py* where we make sure the user associated with a topic matches the currently logged-in user. Put the code for this check in a function called `check_topic_owner()`, and call this function where appropriate.

*These are the three parts of views.py that are affected by this refactoring work:*

```python title="views.py"
...
@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request.user)
    ...

...
@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(topic, request.user)
    ...

def check_topic_owner(topic, user):
    """Make sure the currently logged-in user owns the topic that's 
    being requested.

    Raise Http404 error if the user does not own the topic.
    """
    if topic.owner != user:
        raise Http404
```

*You can also see the full project for this solution [here](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_19/ex_19_3_refactoring).*