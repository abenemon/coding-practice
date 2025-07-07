# Understanding Python’s `round()` Function: A Natural Language Explainer

When you see `round(number, ndigits=None)` in Python’s help system, you’re looking at the **round** function—a way to round numbers to the nearest whole number, or to a specific number of decimal places.

---

## What Is `round` in Python?

- `round` is a built-in function that rounds a number to the nearest integer, or to a specified number of decimal places.
- It works on both integers and floating-point numbers.
- You can choose how many decimal digits to keep (by default, it rounds to the nearest whole number).

---

## What You Write and What Python Does

- **What you write:**  
    `round(number)`  
    `round(number, ndigits)`

- **What Python does:**  
    For built-in number types, Python calls a special method on the number:  
    `number.__round__(ndigits)`  
    (If you only pass one argument, `ndigits` is set to `None`.)

    This means if you create your own class and define a `__round__` method, `round()` will use it!

---

## Parameters

- `number`: The number you want to round. (Can be an `int`, `float`, or any object with a `__round__` method.)
- `ndigits` (optional): How many decimal places to round to.
    - If omitted or `None`, rounds to the nearest integer.
    - If positive, rounds to that many decimal places.
    - If negative, rounds to the left of the decimal point.

---

## What It Returns

- If you omit `ndigits`, or set it to `None`, `round()` returns an **integer**.
- If you provide `ndigits`, the result has the **same type as the number** you gave it (usually a float).

---

## Examples

- **Round to nearest integer (default):**  
      `round(4.3)`        # 4  
      `round(4.8)`        # 5

- **Round to specific decimal places:**  
      `round(3.14159, 2)` # 3.14  
      `round(2.718, 1)`   # 2.7

- **Round to tens, hundreds, etc. (negative ndigits):**  
      `round(1234, -2)`   # 1200

- **With negative numbers:**  
      `round(-2.5)`       # -2

---

## How Does Python Decide Which Way to Round?

- Python uses “round half to even” (also called “banker’s rounding”):  
    If the number is exactly halfway between two possibilities, it rounds to the nearest **even** number.

    Example:  
    `round(2.5)`   # 2 (2 is even)  
    `round(3.5)`   # 4 (4 is even)

---

## Custom Class Example

If you want your own objects to work with `round()`, define a `__round__` method:

    class MyNumber:
        def __init__(self, value):
            self.value = value
        def __round__(self, ndigits=None):
            # Example: always round down to the nearest integer
            return int(self.value)

    x = MyNumber(3.8)
    round(x)     # Calls x.__round__(), returns 3

---

## In summary

- `round()` rounds numbers to the nearest integer, or to a chosen number of decimal places.
- Under the hood, it calls the object's `__round__` method.
- You can control how your own classes round by defining `__round__`.

---

**Tip:**  
To see more, run:

    help(round)

---
