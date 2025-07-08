# Understanding Python’s `int.__abs__` Method: A Natural Language Explainer

When you see `int.__abs__` in Python’s help system, you’re looking at the hidden “magic method” that makes the built-in `abs()` function work with integers.

---

## What Is `__abs__` in Python for `int`?

- `__abs__` is a **special (dunder) method** defined on the `int` type (and other numeric types).
- It tells Python **how to compute the absolute value** of an integer—turning negative numbers positive, and leaving positive numbers unchanged.

---

## What You Write and What Python Does

- **What you write:**  
    `abs(-5)`

- **What Python does:**  
    Calls the dunder method:  
    `(-5).__abs__()`

- Both expressions return `5`.

---

## Parameters

- ``self``: The integer to get the absolute value of.

---

## What It Returns

- The absolute value of the integer as a new integer object.
    - If the number is negative, returns its positive counterpart.
    - If the number is already positive (or zero), returns the number unchanged.

---

## Examples

- **Function form:**  
      `abs(-42)`                    # 42  
      `abs(17)`                     # 17

- **Dunder method form:**  
      `(-42).__abs__()`             # 42  
      `(17).__abs__()`              # 17

- **With variables:**  
      `n = -100; abs(n)`            # 100  
      `n.__abs__()`                 # 100

---

## Quick Notes

- You almost always use the `abs()` function, but knowing about `__abs__` explains how `abs()` works for different types.
- If you define your own class and want `abs(my_object)` to work, implement a `__abs__` method.

---

## In summary

- `int.__abs__` is how Python implements the `abs()` function for integers.
- `abs(n)` is just a shortcut for `n.__abs__()`.
- Other numeric types like `float`, `complex`, and custom classes can have their own `__abs__` implementations.

---

**Tip:**  
To see all special methods on `int`:

    dir(int)

Or to read more about absolute value:

    help(int.__abs__)

---
