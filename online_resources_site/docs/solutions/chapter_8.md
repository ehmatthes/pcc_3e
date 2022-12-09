---
hide:
  - footer
title: "Solutions: Chapter 8"
---

# Solutions - Chapter 8

---

## 8-1: Message

Write a function called `display_message()` that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

```python title="message.py"
def display_message():
    """Display a message about what I'm learning."""
    msg = "I'm learning to store code in functions."
    print(msg)

display_message()
```

``` title="Output:"
I'm learning to store code in functions.
```

## 8-2: Favorite Book

Write a function called `favorite_book()` that accepts one parameter, `title`. The function should print a message, such as `One of my favorite books is Alice in Wonderland.` Call the function, making sure to include a book title as an argument in the function call.

```python title="favorite_book.py"
def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(f"{title} is one of my favorite books.")

favorite_book('The Abstract Wild')
```

``` title="Output:"
The Abstract Wild is one of my favorite books.
```

## 8-3: T-Shirt

Write a function called `make_shirt()` that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.

Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

```python title="t_shirt.py"
def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')
```

``` title="Output:"
I'm going to make a large t-shirt.
It will say, "I love Python!"

I'm going to make a medium t-shirt.
It will say, "Readability counts."
```

## 8-4: Large Shirts

Modify the `make_shirt()` function so that shirts are large by default with a message that reads *I love Python*. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

```python title="large_shirts.py"
def make_shirt(size='large', message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')
```

``` title="Output:"
I'm going to make a large t-shirt.
It will say, "I love Python!"

I'm going to make a medium t-shirt.
It will say, "I love Python!"

I'm going to make a small t-shirt.
It will say, "Programmers are loopy."
```

## 8-5: Cities

Write a function called `describe_city()` that accepts the name of a city and its country. The function should print a simple sentence, such as `Reykjavik is in Iceland.` Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

```python title="cities.py"
def describe_city(city, country='chile'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')
```

``` title="Output:"
Santiago is in Chile.
Reykjavik is in Iceland.
Punta Arenas is in Chile.
```

## 8-6: City Names

Write a function called `city_country()` that takes in the name of a city and its country. The function should return a string formatted like this:

> "Santiago, Chile"

Call your function with at least three city-country pairs, and print the values that are returned.

```python title="city_names.py"
def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"

city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)
```

``` title="Output:"
Santiago, Chile
Ushuaia, Argentina
Longyearbyen, Svalbard
```

## 8-7: Album

Write a function called `make_album()` that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

Use `None` to add an optional parameter to `make_album()` that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.

Simple version:

```python title="album.py"
def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)
```

``` title="Output:"
{'artist': 'Metallica', 'title': 'Ride The Lightning'}
{'artist': 'Beethoven', 'title': 'Ninth Symphony'}
{'artist': 'Willie Nelson', 'title': 'Red-Headed Stranger'}
```

With number of songs:

```python title="album_num_songs.py"
def make_album(artist, title, num_songs=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if num_songs:
        album_dict['num_songs'] = num_songs
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)

album = make_album('iron maiden', 'piece of mind', num_songs=8)
print(album)
```

``` title="Output:"
{'artist': 'Metallica', 'title': 'Ride The Lightning'}
{'artist': 'Beethoven', 'title': 'Ninth Symphony'}
{'artist': 'Willie Nelson', 'title': 'Red-Headed Stranger'}
{'artist': 'Iron Maiden', 'title': 'Piece Of Mind', 'num_songs': 8}
```

## 8-8: User Albums

Start with your program from Exercise 8-7. Write a `while` loop that allows users to enter an album's artist and title. Once you have that information, call `make_album()` with the user's input and print the dictionary that's created. Be sure to include a quit value in the `while` loop.

```python title="user_albums.py"
def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")
```

``` title="Output:"
Enter 'quit' at any time to stop.

What album are you thinking of? number of the beast
Who's the artist? iron maiden
{'artist': 'Iron Maiden', 'title': 'Number Of The Beast'}

What album are you thinking of? touch of class
Who's the artist? angel romero
{'artist': 'Angel Romero', 'title': 'Touch Of Class'}

What album are you thinking of? rust in peace
Who's the artist? megadeth
{'artist': 'Megadeth', 'title': 'Rust In Peace'}

What album are you thinking of? quit

Thanks for responding!
```

## 8-9: Messages

Make a list containing a series of short text messages. Pass the list to a function called `show_messages()`, which prints each text message.

```python title="messages.py"
def show_messages(messages):
    """Print all messages in the list."""
    for message in messages:
        print(message)

messages = ["hello there", "how are u?", ":)"]
show_messages(messages)
```

``` title="Output:"
hello there
how are u?
:)
```

## 8-10: Sending Messages

Start with a copy of your program from Exercise 8-9. Write a function called `send_messages()` that prints each text message and moves each message to a new list called `sent_messages` as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.

```python title="sending_messages.py"
def show_messages(messages):
    """Print all messages in the list."""
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
```

``` title="Output:"
Showing all messages:
hello there
how are u?
:)

Sending all messages:
:)
how are u?
hello there

Final lists:
[]
[':)', 'how are u?', 'hello there']
```

## 8-11: Archived Messages

Start with your work from Exercise 8-10. Call the function `send_messages()` with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

```python title="archived_messages.py"
def show_messages(messages):
    """Print all messages in the list."""
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
```

``` title="Output:"
Showing all messages:
hello there
how are u?
:)

Sending all messages:
:)
how are u?
hello there

Final lists:
['hello there', 'how are u?', ':)']
[':)', 'how are u?', 'hello there']
```

## 8-12: Sandwiches

Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandiwch that is being ordered. Call the function three tiems, using a different number of arguments each time.

```python title="sandwiches.py"
def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(f"  ...adding {item} to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')
```

``` title="Output:"
I'll make you a great sandwich:
  ...adding roast beef to your sandwich.
  ...adding cheddar cheese to your sandwich.
  ...adding lettuce to your sandwich.
  ...adding honey dijon to your sandwich.
Your sandwich is ready!

I'll make you a great sandwich:
  ...adding turkey to your sandwich.
  ...adding apple slices to your sandwich.
  ...adding honey mustard to your sandwich.
Your sandwich is ready!

I'll make you a great sandwich:
  ...adding peanut butter to your sandwich.
  ...adding strawberry jam to your sandwich.
Your sandwich is ready!
```

8-14: Cars
---

Write a function that stores information about a car in a dictionary. the function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:

```python
car = make_car('subaru', 'outback', color='blue', tow_package=True)
```

Print the dictionary that's returned to make sure all the information was stored correctly.

```python title="cars.py"
def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_old_accord)
```

``` title="Output:"
{'manufacturer': 'Subaru', 'model': 'Outback', 'color': 'blue', 'tow_package': True}
{'manufacturer': 'Honda', 'model': 'Accord', 'year': 1991, 'color': 'white', 'headlights': 'popup'}
```

8-15: Printing Models
---

Put the functions for the example *printing_models.py* in a separate file called *printing_functions.py*. Write an `import` statement at the top of *printing_models.py*, and modify the file to use the imported functions.

*printing_functions.py:*

```python title="printing_functions.py"
"""Functions related to printing 3d models."""

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until there are none left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
    
        # Simulate creating a 3d print from the design.
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
```

*printing_models.py:*

```python title="printing_models.py"
import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
```

``` title="Output:"
Printing model: dodecahedron
Printing model: robot pendant
Printing model: iphone case

The following models have been printed:
dodecahedron
robot pendant
iphone case
```
