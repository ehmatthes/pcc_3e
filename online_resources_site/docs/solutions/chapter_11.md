---
hide:
  - footer
title: "Solutions: Chapter 11"
---

# Solutions - Chapter 11

---

## 11-1: City, Country

Write a function that accepts two parameters: a city name and a country name. The function should return a single string of the form *City, Country*, such as `Santiago, Chile`. Store the function in a module called *city_functions.py*, and save this file in a new folder so `pytest` won’t try to run the tests we’ve already written.

Create a file called *test_cities.py* that tests the function you just wrote. Write a function called `test_city_country()` to verify that calling your function with values such as `'santiago'` and `'chile'` results in the correct string. Run the test, and make sure `test_city_country()` passes.

```python title="city_country/city_functions.py"
"""A collection of functions for working with cities."""

def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"
```

***Note:** This is the same function we wrote in [Exercise 8-6](../chapter_8/#8-6-city-names).*

```python title="city_country/test_cities.py"
from city_functions import city_country

def test_city_country():
    """Does a simple city and country pair work?"""
    santiago_chile = city_country('santiago', 'chile')
    assert santiago_chile == 'Santiago, Chile'
```

``` title="Output:"
city_country $ pytest
============================ test session starts =============================
platform darwin -- Python 3.10.0, pytest-7.1.2, pluggy-1.0.0
rootdir: /.../solution_files/chapter_11/city_country
collected 1 item                                                             

test_cities.py .                                                       [100%]
============================= 1 passed in 0.01s ==============================
```

## 11-2: Population

Modify your function so it requires a third parameter, `population`. It should now return a single string of the form `City, Country - population xxx`, such as `Santiago, Chile - population 5000000`. Run *test_cities.py* again. Make sure `test_city_country()` fails this time.

Modify the function so the `population` parameter is optional. Run the test, and make sure `test_city_country()` passes again.

Write a second test called `test_city_country_population()` that verifies you can call your function with the values `'santiago'`, `'chile'`, and `'population=5000000'`. Run the tests one more time, and make sure this new test passes.

```python title="population/city_functions.py"
"""A collection of functions for working with cities."""

def city_country(city, country, population):
    """Return a string like 'Santiago, Chile - population 5000000'."""
    output_string = f"{city.title()}, {country.title()}"
    output_string += f" -population {population}"
    return output_string
```

``` title="Output:"
population $ pytest
============================ test session starts =============================
platform darwin -- Python 3.10.0, pytest-7.1.2, pluggy-1.0.0
rootdir: /.../solution_files/chapter_11/population
collected 1 item                                                             

test_cities.py F                                                       [100%]

================================== FAILURES ==================================
_____________________________ test_city_country ______________________________

    def test_city_country():
        """Does a simple city and country pair work?"""
>       santiago_chile = city_country('santiago', 'chile')
E       TypeError: city_country() missing 1 required positional argument: 'population'

test_cities.py:5: TypeError
========================== short test summary info ===========================
FAILED test_cities.py::test_city_country - TypeError: city_country() missin...
============================= 1 failed in 0.09s ==============================
```

```python title="population/city_functions_optional.py"
"""A collection of functions for working with cities."""

def city_country(city, country, population=0):
    """Return a string representing a city-country pair."""

    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - population {population}"
    return output_string
```

``` title="Output:"
population $ pytest
============================ test session starts =============================
platform darwin -- Python 3.10.0, pytest-7.1.2, pluggy-1.0.0
rootdir: /.../solution_files/chapter_11/population
collected 1 item                                                             

test_cities.py .                                                       [100%]
============================= 1 passed in 0.01s ==============================
```

```python title="population/test_cities.py"
from city_functions_pop_optional import city_country

def test_city_country():
    """Does a simple city and country pair work?"""
    santiago_chile = city_country('santiago', 'chile')
    assert santiago_chile == 'Santiago, Chile'

def test_city_country_population():
    """Can I include a population argument?"""
    santiago_chile = city_country('santiago', 'chile', population=5_000_000)
    assert santiago_chile == 'Santiago, Chile - population 5000000'
```

**Note:** I have two versions of the `city_functions.py` module saved in the solution files, so the `import` statement here has changed to use the updated version of the function.

``` title="Output:"
population $ pytest
============================ test session starts =============================
platform darwin -- Python 3.10.0, pytest-7.1.2, pluggy-1.0.0
rootdir: /.../solution_files/chapter_11/population
collected 2 items                                                            

test_cities.py ..                                                      [100%]
============================= 2 passed in 0.01s ==============================
```

## 11-3: Employee

Write a class called `Employee`. The `__init__()` method should take in a first name, a last name, and an annual salary, and store each of these as attributes. Write a method called `give_raise()` that adds $5000 to the annual salary by default but also accepts a different raise amount.

Write a test file for `Employee` with two test functions, `test_give_default_raise()` and `test_give_custom_raise()`. Write your tests once without using a fixture, and make sure they both pass. Then write a fixture so you don’t have to create a new employee instance in each test function. Run the tests again, and make sure both tests still pass.

```python title="employee/employee.py"
class Employee:
    """A class to represent an employee."""

    def __init__(self, f_name, l_name, salary):
        """Initialize the employee."""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.salary += amount
```

```python title="employee/test_employee.py"
from employee import Employee

def test_give_default_raise():
    """Test that a default raise works correctly."""
    employee = Employee('eric', 'matthes', 65_000)
    employee.give_raise()
    assert employee.salary == 70_000

def test_give_custom_raise():
    """Test that a custom raise works correctly."""
    employee = Employee('eric', 'matthes', 65_000)
    employee.give_raise(10000)
    assert employee.salary == 75_000
```

``` title="Output:"
employee $ pytest
============================ test session starts =============================
platform darwin -- Python 3.10.0, pytest-7.1.2, pluggy-1.0.0
rootdir: /.../solution_files/chapter_11/employee
collected 2 items                                                            

test_employee.py ..                                                    [100%]
============================= 2 passed in 0.01s ==============================
```

```python title="employee_with_fixture/employee.py"
class Employee:
    """A class to represent an employee."""

    def __init__(self, f_name, l_name, salary):
        """Initialize the employee."""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.salary += amount
```

```python title="employee_with_fixture/test_employee.py"
import pytest

from employee import Employee

@pytest.fixture
def employee():
    """An Employee object that will be available to all test functions."""
    employee = Employee('eric', 'matthes', 65_000)
    return employee

def test_give_default_raise(employee):
    """Test that a default raise works correctly."""
    employee.give_raise()
    assert employee.salary == 70_000

def test_give_custom_raise(employee):
    """Test that a custom raise works correctly."""
    employee.give_raise(10000)
    assert employee.salary == 75_000
```

``` title="Output:"
employee_with_fixture $ pytest
============================ test session starts =============================
platform darwin -- Python 3.10.0, pytest-7.1.2, pluggy-1.0.0
rootdir: /.../solution_files/chapter_11/employee_with_fixture
collected 2 items                                                            

test_employee.py ..                                                    [100%]
============================= 2 passed in 0.01s ==============================
```