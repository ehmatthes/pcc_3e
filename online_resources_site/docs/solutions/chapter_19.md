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

*These are the three parts of views.py that are affected by this refactoring work. You can also see the full project for this solution [here](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_19/ex_19_3_refactoring).*

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

## 19-4: Protecting `new_entry`

Currently, a user can add a new entry to another user’s learning log by entering a URL with the ID of a topic belonging to another user. Prevent this attack by checking that the current user owns the entry’s topic before saving the new entry.

*Note: This solution builds on the refactoring done in 19-3. You can see the full project for this solution [here](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_19/ex_19_4_protecting_new_entry).*

```python title="views.py"
...
@login_required    
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request.user)
    ...

...
def check_topic_owner(topic, user):
    """Make sure the currently logged-in user owns the topic that's 
    being requested.

    Raise Http404 error if the user does not own the topic.
    """
    if topic.owner != user:
        raise Http404
```

## 19-5: Protected Blog

In your Blog project, make sure each blog post is connected to a particular user. Make sure all posts are publicly accessible but only registered users can add posts and edit existing posts. In the view that allows users to edit their posts, make sure the user is editing their own post before processing the form.

*You can see the full project for this solution [here](https://github.com/ehmatthes/pcc_3e/tree/main/solution_files/chapter_19/ex_19_5_protected_blog).*