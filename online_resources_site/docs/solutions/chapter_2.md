---
hide:
  - footer
title: "Solutions: Chapter 2"
---

# Solutions - Chapter 2

---

## 2-1: Simple Message

Assign a message to a variable, and then print that message.

```python title="simple_message.py"
msg = "I love learning to use Python."
print(msg)
```

``` title="Output:"
I love learning to use Python.
```

## 2-2: Simple Messages

Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message.

```python title="simple_messages.py"
msg = "I love learning to use Python."
print(msg)

msg = "It's really satisfying!"
print(msg)
```

``` title="Output:"
I love learning to use Python.
It's really satisfying!
```

## 2-3: Personal Message

Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

```python title="personal_message.py"
name = "eric"
msg = f"Hello {name.title()}, would you like to learn some Python today?"

print(msg)
```

``` title="Output:"
Hello Eric, would you like to learn some Python today?
```

## 2-4: Name Cases

Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

```python title="name_cases.py"
name = "eric"

print(name.lower())
print(name.upper())
print(name.title())
```

``` title="Output:"
eric
ERIC
Eric
```

## 2-5: Famous Quote

Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:

> Albert Einstein once said, "A person who never made a mistake never tried anything new."

```python title="famous_quote.py"
print('Albert Einstein once said, "A person who never made a mistake')
print('never tried anything new."')
```

``` title="Output:"
Albert Einstein once said, "A person who never made a mistake
never tried anything new."
```

## 2-6: Famous Quote 2

Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called `famous_person`. Then compose your message and represent it with a new variable called `message`. Print your message.

```python title="famous_quote_2.py"
famous_person = "Albert Einstein"

message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'

print(message)
```

``` title="Output:"
Albert Einstein once said, "A person who never made a mistake never tried anything new."
```

??? note
    The line that defines `message` in this file is longer than we'd typically like to write. You'll see this a little later in Chapter 7, but you can add to a string using the `+=` operator. So this program could also be written like this, with exactly the same output:

    ```python title="famous_quote_3.py"
    famous_person = "Albert Einstein"

    message = f'{famous_person} once said, "A person who never made a mistake'
    message += ' never tried anything new."'

    print(message)
    ```


## 2-7: Stripping Names

Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, `"\t"` and `"\n"`, at least once.

Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, `lstrip()`, `rstrip()`, and `strip()`.

```python title="stripping_names.py"
name = "\tEric Matthes\n"

print("Unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())
```

``` title="Output:"
Unmodified:
    Eric Matthes


Using lstrip():
Eric Matthes


Using rstrip():
    Eric Matthes

Using strip():
Eric Matthes
```

## 2-8: File Extensions

Python has a `removesuffix()` method that works exactly like `removeprefix()`. Assign the value 'python_notes.txt' to a variable called `filename`. Then use the `removesuffix()` method to display the filename without the file extension, like some file browsers do.

```python title="file_extensions.py"
filename = 'python_notes.txt'
simple_filename = filename.removesuffix('.txt')

print(simple_filename)
```

``` title="Output:"
python_notes
```

## 2-10: Favorite Number

Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number. Print that message.

```python title="favorite_number.py"
fav_num = 42
msg = f"My favorite number is {fav_num}."

print(msg)
```

``` title="Output:"
My favorite number is 42.
```
