---
hide:
  - footer
title: "Solutions: Chapter 4"
---

# Solutions - Chapter 4

---

## 4-1: Pizzas

Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a `for` loop to print the name of each pizza.

- Modify your `for` loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like *I like pepperoni pizza.*
- Add a line at the end of your program, outside the `for` loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as *I really love pizza!*

```python title="pizzas.py"
favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']

# Print the names of all the pizzas.
for pizza in favorite_pizzas:
    print(pizza)

print("\n")

# Print a sentence about each pizza.
for pizza in favorite_pizzas:
    print(f"I really love {pizza} pizza!")

print("\nI really love pizza!")
```

``` title="Output:"
pepperoni
hawaiian
veggie

I really love pepperoni pizza!
I really love hawaiian pizza!
I really love veggie pizza!

I really love pizza!
```

## 4-2: Animals

Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a `for` loop to print out the name of each animal.
- Modify your program to print a statement about each animal, such as *A dog would make a great pet.*
- Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as *Any of these animals would make a great pet!*

```python title="animals.py"
animals = ["spider monkey", "lemur", "giraffe"]

# Print each animal.
for animal in animals:
    print(animal)

print("\n")

# Print a statement about each animal.
for animal in animals:
    print(f"A {animal} has a long tail.")

print("\nAll of these animals have long tails.")
```

``` title="Output:"
spider monkey
lemur
giraffe

A spider monkey has a long tail.
A lemur has a long tail.
A giraffe has a long tail.

All of these animals have long tails.
```

## 4-3: Counting to Twenty

Use a `for` loop to print the numbers from 1 to 20, inclusive.

```python title="counting_to_twenty.py"
numbers = list(range(1, 21))

for number in numbers:
    print(number)
```

``` title="Output:"
1
2
3
...
18
19
20
```

## 4-5: Summing a Million

Make a list of the numbers from one to one million, and then use `min()` and `max()` to make sure your list actually starts at one and ends at one million. Also, use the `sum()` function to see how quickly Python can add a million numbers.

```python title="summing_a_million.py"
numbers = list(range(1, 1_000_001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))
```

``` title="Output:"
1
1000000
500000500000
```

## 4-6: Odd Numbers

Use the third argument of the `range()` function to make a list of the odd numbers from 1 to 20. Use a `for` loop to print each number.

```python title="odd_numbers.py"
odd_numbers = list(range(1, 20, 2))

for number in odd_numbers:
    print(number)
```

``` title="Output:"
1
3
5
...
15
17
19
```

## 4-7: Threes

Make a list of the multiples of 3 from 3 to 30. Use a `for` loop to print the numbers in your list.

```python title="threes.py"
threes = list(range(3, 31, 3))

for number in threes:
    print(number)
```

``` title="Output:"
3
6
9
...
24
27
30
```

## 4-8: Cubes

A number raised to the third power is called a *cube*. For example, the cube of 2 is written as `2**3` in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a `for` loop to print out the value of each cube.

```python title="cubes.py"
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)
```

``` title="Output:"
1
8
27
...
512
729
1000
```

## 4-9: Cube Comprehension

Use a list comprehension to generate a list of the first 10 cubes.

```python title="cube_comprehension.py"
cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)
```

``` title="Output:"
1
8
27
...
512
729
1000
```

## 4-11: My Pizzas, Your Pizzas

Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it `friend_pizzas`. Then, do the following:

- Add a new pizza to the original list.
- Add a different pizza to the list `friend_pizzas`.
- Prove that you have two separate lists. Print the message, *My favorite pizzas are:*, and then use a `for` loop to print the first list. Print the message, *My friend's favorite pizzas are:*, and then use a `for` loop to print the second list. Make sure each new pizza is stored in the appropriate list.

```python title="my_pizzas_your_pizzas.py"
favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("meat lover's")
friend_pizzas.append('pesto')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
```

``` title="Output:"
My favorite pizzas are:
- pepperoni
- hawaiian
- veggie
- meat lover's

My friend's favorite pizzas are:
- pepperoni
- hawaiian
- veggie
- pesto
```

## 4-12: More Loops

All versions of *foods.py* in this section have avoided using `for` loops when printing, to save space. Choose a version of *foods.py*, and write two `for` loops to print each list of foods.

```python title="more_loops.py"
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(f"- {food}")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"- {food}")
```

``` title="Output:"
My favorite foods are:
- pizza
- falafel
- carrot cake
- cannoli

My friend's favorite foods are:
- pizza
- falafel
- carrot cake
- ice cream
```

## 4-13: Buffet

A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

- Use a `for` loop to print each food the restaurant offers.
- Try to modify one of the items, and make sure that Python rejects the change.
- The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a `for` loop to print each of the items on the revised menu.

```python title="buffet.py"
menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
    )

print("You can choose from the following menu items:")
for item in menu_items:
    print(f"- {item}")

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'black cod tips', 'king crab legs',
    )

print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in menu_items:
    print(f"- {item}")
```

``` title="Output:"
You can choose from the following menu items:
- rockfish sandwich
- halibut nuggets
- smoked salmon chowder
- salmon burger
- crab cakes

Our menu has been updated.
You can now choose from the following items:
- rockfish sandwich
- halibut nuggets
- smoked salmon chowder
- black cod tips
- king crab legs
```
