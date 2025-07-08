# Understanding Python’s `str.upper` Method: A Natural Language Explainer

When you see `str.upper` in Python’s help system, you’re looking at the method that converts all the letters in a string to uppercase.

---

## What Is `upper` in Python for Strings?

- `upper` is an **instance method** of the `str` type.
- It returns a **new string** with all characters converted to uppercase (capital letters).
- The **original string is not changed**—strings are immutable in Python.

---

## What You Write and What Python Does

- **What you write:**  
    `"hello world".upper()`

- **What Python does:**  
    Returns a new string where every lowercase letter in the original has been replaced by its uppercase version.  
    - Under the hood, Python runs:  
      `"hello world".upper()`

---

## Parameters

- No parameters (other than `self`, the string itself).

---

## What It Returns

- A **new string** in which all cased characters are uppercase.
- The original string is unchanged.

---

## Examples

- **Basic usage:**  
      `"hello world".upper()`          # 'HELLO WORLD'

- **String with mixed case:**  
      `"PyThOn".upper()`               # 'PYTHON'

- **String with numbers and symbols:**  
      `"hello123!".upper()`            # 'HELLO123!'

- **String with no lowercase letters:**  
      `"123!@#".upper()`               # '123!@#' (unchanged)

---

## Quick Notes

- Only cased letters (a–z) are affected. Numbers, symbols, and already-uppercase letters stay the same.
- **Strings are immutable**: the original string is not changed, even though you call a method on it.

---

## In summary

- `str.upper` returns a new string with all letters in uppercase.
- The original string remains unchanged.

---

**Tip:**  
To see more, run:

    help(str.upper)

---
