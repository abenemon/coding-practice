# Understanding Boolean Operators in Python

Boolean operators are special keywords that let you combine, compare, and manipulate true/false (boolean) values in Python. They’re a fundamental part of writing conditions, controlling logic, and making decisions in your code.

## What Are Boolean Values?

- Python has two built-in boolean values:
  - ``True``
  - ``False``

## The Three Main Boolean Operators

Python uses three main boolean (logical) operators:

- **and**  
  Returns ``True`` if *both* sides are true.

- **or**  
  Returns ``True`` if *at least one* side is true.

- **not**  
  Flips ``True`` to ``False``, and ``False`` to ``True``.

## Basic Usage

- **and operator:**
  - ``True and True``     # returns True
  - ``True and False``    # returns False

- **or operator:**
  - ``True or False``     # returns True
  - ``False or False``    # returns False

- **not operator:**
  - ``not True``          # returns False
  - ``not False``         # returns True

    ``a = True
    b = False
    result = a and not b    # True and True -> True
    ``

## Using Boolean Operators in Conditions

- Combine comparisons for complex logic:
  - ``x = 5
    y = 10
    if x > 0 and y > 0:
        print("Both positive")
    ``

- Chain multiple conditions:
  - ``score = 85
    if score >= 90 or score == 85:
        print("Great job!")
    ``

## Truthy and Falsy Values

- Python treats some values as ``True`` and some as ``False`` in boolean contexts:
  - **Falsy values:** ``0``, ``''`` (empty string), ``[]`` (empty list), ``None``, ``False``
  - **Truthy values:** Anything else

  - ``if [] or 0:
        print("Will not print!")   # Both are falsy
    if 1 and "hello":
        print("This prints!")      # Both are truthy
    ``

## Examples

- **Checking multiple conditions:**
  - ``age = 20
    has_id = True
    if age >= 18 and has_id:
        print("You can enter")
    ``

- **Using not to reverse a condition:**
  - ``logged_in = False
    if not logged_in:
        print("Please log in")
    ``

- **Combining or and and:**
  - ``x = 5
    y = 0
    if x > 0 or y > 0:
        print("At least one is positive")
    ``

    ``num = 7
    if num > 0 and (num % 2 == 1 or num % 5 == 0):
        print("Special number")
    ``

## In Summary

- Use ``and`` to require *all* conditions to be true.
- Use ``or`` to require *at least one* condition to be true.
- Use ``not`` to flip the truth value.
- Boolean operators help you write smarter, more flexible programs.

Tip: Use parentheses ``( )`` to group conditions and make your logic clear!

