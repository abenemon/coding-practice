# Understanding Python’s Comparison Methods: A Natural Language Guide

Python uses special “dunder” methods (double-underscore methods) to let objects compare themselves to other objects. These comparison methods let you use operators like `<`, `<=`, `>`, `>=`, `==`, and `!=` with all sorts of objects—not just numbers!

---

## What Are Comparison Methods?

- **Comparison methods** are special methods you can define in your class so Python knows how to compare your objects.
- If you use a comparison operator (like `x < y`), Python actually calls a method with a name like `__lt__` (“less than”) under the hood.

---

## The Six Main Comparison Methods

Here are the most common comparison methods and what operator triggers them:

| Operator | What you write     | What Python does         | Method name   | What it means                          |
|----------|-------------------|-------------------------|-------------- |----------------------------------------|
| `<`      | `x < y`           | `x.__lt__(y)`           | __lt__        | Less than                              |
| `<=`     | `x <= y`          | `x.__le__(y)`           | __le__        | Less than or equal to                  |
| `>`      | `x > y`           | `x.__gt__(y)`           | __gt__        | Greater than                           |
| `>=`     | `x >= y`          | `x.__ge__(y)`           | __ge__        | Greater than or equal to               |
| `==`     | `x == y`          | `x.__eq__(y)`           | __eq__        | Equal to                               |
| `!=`     | `x != y`          | `x.__ne__(y)`           | __ne__        | Not equal to                           |

---

## What You Write and What Python Does

For each comparison operator, Python calls a corresponding method on the **left-hand** object:

- **What you write:**  
    `a < b`

- **What Python does:**  
    `a.__lt__(b)`  
    (tries to call the left side’s `__lt__` method, if it exists)

---

## What Does That Mean for Custom Classes?

If you create your own class and want it to work with `<`, `==`, etc., you need to define these methods in your class.  
Here’s an example for `__lt__` (less than):

    class Card:
        def __init__(self, rank):
            self.rank = rank
        def __lt__(self, other):
            return self.rank < other.rank

    c1 = Card(3)
    c2 = Card(5)
    print(c1 < c2)      # True (calls c1.__lt__(c2))

You can define as many or as few of these as you need. If you leave some out, those comparisons may not be allowed (Python will raise an error).

---

## Why Use These Methods?

- They let Python know how to sort, compare, or check equality for your objects.
- Functions like `sorted()`, `min()`, and `max()` rely on these methods to decide the order.

---

## Notes on Comparison Methods

- If you don’t define these in your class, comparing objects usually gives a `TypeError` (unless the class inherits them from a parent class).
- For **equality** (`==` and `!=`), if you don’t define `__eq__`, comparing objects usually just checks if they are the *same object* in memory (not if they have the same contents).
- **Not all** comparisons are automatically inferred—defining `__lt__` doesn’t mean `__le__` or `__gt__` will work unless you define those too (but see functools.total_ordering in the standard library for a shortcut).

---

## Quick Reference Table

| Method    | Operator | Example call       | Should return  |
|-----------|----------|-------------------|----------------|
| __lt__    | `<`      | `a.__lt__(b)`     | True/False     |
| __le__    | `<=`     | `a.__le__(b)`     | True/False     |
| __gt__    | `>`      | `a.__gt__(b)`     | True/False     |
| __ge__    | `>=`     | `a.__ge__(b)`     | True/False     |
| __eq__    | `==`     | `a.__eq__(b)`     | True/False     |
| __ne__    | `!=`     | `a.__ne__(b)`     | True/False     |

---

## In summary

- Python’s comparison operators work by calling special double-underscore methods on objects.
- You can control how your own classes compare by defining `__lt__`, `__le__`, `__gt__`, `__ge__`, `__eq__`, and `__ne__`.
- This lets your objects work with sorting, equality checks, and more.

---

**Tip:**  
To see which comparison methods a built-in type supports, run:

    dir(int)
    dir(str)
    dir(list)

Or, for your own class, check which dunder methods you’ve defined!

---
