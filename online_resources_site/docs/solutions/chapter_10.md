---
hide:
  - footer
title: "Solutions: Chapter 10"
---

# Solutions - Chapter 10

---

## 10-1: Learning Python

Open a blank file in your text editor and write a few lines summarizing what you've learned about Python so far. Start each line with the phrase *In Python you can...* Save the file as *learning_python.txt* in the same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote two times: print the contents once by reading in the entire file, and once by storing the lines in a list and then looping over each line.

``` title="learning_python.txt"
In Python you can store as much information as you want.
In Python you can connect pieces of information.
In Python you can model real-world situations.
```

```python title="learning_python.py"
from pathlib import Path

print("--- Reading in the entire file:")
path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

print("\n--- Looping over the lines:")
lines = contents.splitlines()
for line in lines:
    print(line)
```

``` title="Output:"
--- Reading in the entire file:
In Python you can store as much information as you want.
In Python you can connect pieces of information.
In Python you can model real-world situations.

--- Looping over the lines:
In Python you can store as much information as you want.
In Python you can connect pieces of information.
In Python you can model real-world situations.
```

## 10-2: Learning C

You can use the `replace()` method to replace any word in a string with a different word. Here's a quick example showing how to replace `'dog'` with `'cat'` in a sentence:

```python
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
```

Read in each line from the file you just created, *learning_python.txt*, and replace the word *Python* with the name of another language, such as *C*. Print each modified line to the screen.

```python title="learning_c.py"
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line)

```

``` title="Output:"
In C you can store as much information as you want.
In C you can connect pieces of information.
In C you can model real-world situations.
```

## 10-3: Simpler Code

The program *file_reader.py* in this section uses a temporary variable, `lines`, to show how `splitlines()` works. You can skip the temporary variable and loop directly over the list that `splitlines()` returns:

```
for line in contents.splitlines():
```

Remove the temporary variable from each of the programs in this section, to make them more concise.

```python title="simpler_code_file_reader.py"
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
  print(line)
```

``` title="Output:"
3.1415926535
  8979323846
  2643383279
```

```python title="simpler_code_pi_string.py"
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
```

``` title="Output:"
3.14159265358979323846264338327950288419716939937510...
1000002
```

```python title="simpler_code_pi_birthday.py"
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
```

``` title="Output:"
Enter your birthday, in the form mmddyy: 040122
Your birthday appears in the first million digits of pi!
```

## 10-4: Guest

Write a program that prompts the user for their name. When they respond, write their name to a file called *guest.txt*.

```python title="guest.py"
from pathlib import Path

path = Path('guest.txt')

name = input("What's your name? ")
path.write_text(name)
```

``` title="Output:"
What's your name? eric
```

``` title="guest.txt"
eric
```

## 10-5: Guest Book

Write a `while` loop that prompts users for their name. Collect all the names that are entered, and then write these names to a file called *guest_book.txt*. Make sure each entry appears on a new line in the file.

```python title="guest_book.py"
from pathlib import Path

path = Path('guest_book.txt')

prompt = "\nHi, what's your name? "
prompt += "\nEnter 'quit' if you're the last guest. "

guest_names = []
while True:
    name = input(prompt)
    if name == 'quit':
        break

    print(f"Thanks {name}, we'll add you to the guest book.")
    guest_names.append(name)

# Build a string where "\n" is added after each name.
file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)
```

``` title="Output:"
Hi, what's your name? 
Enter 'quit' if you're the last guest. eric
Thanks eric, we'll add you to the guest book.

Hi, what's your name? 
Enter 'quit' if you're the last guest. erin
Thanks erin, we'll add you to the guest book.

Hi, what's your name? 
Enter 'quit' if you're the last guest. ever
Thanks ever, we'll add you to the guest book.

Hi, what's your name? 
Enter 'quit' if you're the last guest. willie
Thanks willie, we'll add you to the guest book.

Hi, what's your name? 
Enter 'quit' if you're the last guest. quit
```

``` title="guest_book.txt"
eric
erin
ever
willie
```

## 10-6: Addition

One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an `int`, you'll get a `ValueError`. Write a program that prompts for two numbers. Add them together and print the result. Catch the `ValueError` if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.

```python title="addition.py"
try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)
except ValueError:
    print("Sorry, I really needed a number.")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")
```

``` title="Output with two integers:"
Give me a number: 23
Give me another number: 47
The sum of 23 and 47 is 70.
```

``` title="Output with non-numerical input:"
Give me a number: 23
Give me another number: fred
Sorry, I really needed a number.
```

## 10-7: Addition Calculator

Wrap your code from Exercise 10-6 in a `while` loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.

```python title="addition_calculator.py"
print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")
```

``` title="Output:"
Enter 'q' at any time to quit.

Give me a number: 23
Give me another number: 47
The sum of 23 and 47 is 70.

Give me a number: three
Sorry, I really needed a number.

Give me a number: 3
Give me another number: five
Sorry, I really needed a number.

Give me a number: -12
Give me another number: 20
The sum of -12 and 20 is 8.

Give me a number: q
```

## 10-8: Cats and Dogs

Make two files, `cats.txt` and `dogs.txt`. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a `try-except` block to catch the `FileNotFound` error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the `except` block executes properly.

``` title="cats.txt"
henry
clarence
mildred
```

``` title="dogs.txt"
willie
annahootz
summit
```

```python title="cats_and_dogs.py"
from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")

    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")
    else:
        print(contents)
```

``` title="Output with both files:"
Reading file: cats.txt
henry
clarence
mildred

Reading file: dogs.txt
willie
annahootz
summit
```

``` title="Output after moving cats.txt:""
Reading file: cats.txt
  Sorry, I can't find that file.

Reading file: dogs.txt
willie
annahootz
summit
```

## 10-9: Silent Cats and Dogs

Modify your `except` block in Exercise 10-8 to fail silently if either file is missing.

```python title="silent_cats_and_dogs.py"
from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {filename}")
        print(contents)
```

``` title="Output when both files exist:"
Reading file: cats.txt
henry
clarence
mildred

Reading file: dogs.txt
willie
annahootz
summit
```

``` title="Output when cats.txt has been moved:"
Reading file: dogs.txt
willie
annahootz
summit
```

## 10-10: Common Words

Visit [Project Gutenberg](https://gutenberg.org/) and find a few texts you'd like to analyze. Download the text files for these works, or copy the raw text from your browser into a text file on your computer.

You can use the `count()` method to find out how many times a word or phrase appears in a string. For example, the following code counts the number of times `'row'` appers in a string:

```
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3 
```

Notice that converting the string to lowercase using `lower()` catches all appearances of the word you're looking for, regardless of how it's formatted.

Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text. This will be an approximation because it will also count words such as 'then' and 'there'. Try counting 'the ', with a space in the string, and see how much lower your count is.

```python title="common_words.py"
from pathlib import Path

def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    # Note: This is a really simple approximation, and the number returned
    #   will be higher than the actual count.
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)

filename = 'alice.txt'
count_common_words(filename, 'the')
```

``` title="Output:"
'the' appears in alice.txt about 2528 times.
```

This solution only examines one text, but the function can be applied to any number of texts.

## 10-11: Favorite Number

Write a program that prompts for the user's favorite number. Use `json.dumps()` to store this number in a file. Write a separate program that reads in this value and prints the message, "I know your favorite number! It's _____."

```python title="favorite_number_writer.py"
from pathlib import Path
import json

number = input("What's your favorite number? ")

path = Path('favorite_number.json')
contents = json.dumps(number)
path.write_text(contents)

print("Thanks! I'll remember that number.")
```

``` title="Output:"
What's your favorite number? 42
Thanks! I'll remember that number.
```

```python title="favorite_number_reader.py"
from pathlib import Path
import json

path = Path('favorite_number.json')
contents = path.read_text()
number = json.loads(contents)

print(f"I know your favorite number! It's {number}.")
```

``` title="Output:"
I know your favorite number! It's 42.
```

## 10-12: Favorite Number Remembered

Combine the two programs from Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user's favorite number and store it in a file. Run the program twice to see that it works.

```python title="favorite_number_remembered.py"
from pathlib import Path
import json

path = Path('favorite_number.json')
try:
    contents = path.read_text()
except FileNotFoundError:
    number = input("What's your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("Thanks, I'll remember that.")
else:
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")
```

``` title="Output, first run:"
What's your favorite number? 42
Thanks, I'll remember that.
```

``` title="Output, second run:"
I know your favorite number! It's 42.
```

## 10-13: User Dictionary

The *remember_me.py* example only stores one piece of information, the username. Expand this example by asking for two more pieces of information about the user, then store all the information you collect in a dictionary. Write this dictionary to a file using `json.dumps()`, and read it back in using `json.loads()`. Print a summary showing exactly what your program remembers about the user.

```python title="user_dictionary.py"
from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None

def get_new_user_info(path):
    """Get information from a new user."""
    username = input("What is your name? ")
    game = input("What's your favorite game? ")
    animal = input("What's your favorite animal? ")

    user_dict = {
        'username': username,
        'game': game,
        'animal': animal,
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict

def greet_user():
    """Greet the user by name, and state what we know about them."""
    path = Path('user_info.json')
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['username']}!")
        print(f"Hope you've been playing some {user_dict['game']}. ")
        print(f"Have you seen a {user_dict['animal']} recently?")
    else:
        user_dict = get_new_user_info(path)
        msg = f"We'll remember you when you return, {user_dict['username']}!"
        print(msg)

greet_user()
```

``` title="Output, first run:"
What is your name? eric
What's your favorite game? chess
What's your favorite animal? mountain goat
We'll remember you when you return, eric!
```

``` title="Output, second run:"
Welcome back, eric!
Hope you've been playing some chess. 
Have you seen a mountain goat recently?
```

## 10-14: Verify User

The final listing for *remember_me.py* assumes either that the user has already entered their username or that the program is running for the first time. We should modify it in case the current user is not the person who last used the program.

Before printing a welcome back message in `greet_user()`, ask the user if this is the correct username. If it's not, call `get_new_username()` to get the correct username.

```python title="verify_user.py"
from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")    
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
```

``` title="Output:"
> python verify_user.py
What is your name? eric
We'll remember you when you come back, eric!

> python verify_user.py
Are you eric? (y/n) y
Welcome back, eric!

> python verify_user.py
Are you eric? (y/n) n
What is your name? ever
We'll remember you when you come back, ever!

> python verify_user.py
Are you ever? (y/n) y
Welcome back, ever!
```

You might notice the identical `else` blocks in this version of `greet_user()`. One way to clean this function up is to use an empty `return` statement. An empty `return` statement tells Python to leave the function without running any more code in the function.

Here's a cleaner version of `greet_user()`:

```python title="verify_user_clean.py"
def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
            return

    # We got a username, but it's not correct.
    #   Prompt for a new username.
    username = get_new_username(path)
    print(f"We'll remember you when you come back, {username}!")
```

The `return` statement means the code in the function stops running after printing the welcome back message. When the username doesn't exist, or the username is incorrect, the `return` statement is never reached. The second part of the function will only run when the `if` statements fail, so we don't need an `else` block. Now the function prompts for a new username when either `if` statement fails.

The only thing left to address is the nested `if` statements. This can be cleaned up by moving the code that checks whether the username is correct to a separate function. If you're enjoying this exercise, you might try making a new function called `check_username()` and see if you can remove the nested `if` statement from `greet_user()`.
