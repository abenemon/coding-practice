# Understanding Python’s `str.capitalize()` Method: A Natural Language Explainer

When you see `str.capitalize()` in Python’s help system, you’re learning about a string method that changes how the first letter of a string looks.

---

## What Is `capitalize` in Python?

- `capitalize` is a method belonging to **string objects** (things like `"hello"`).
- It returns a **new string** with the first character in uppercase and the rest in lowercase.

---

## What You Write and What Python Does

- **What you write:**  
    `my_string.capitalize()`

- **What Python does:**  
    Takes your string and returns a new string where:
    - The first character is uppercase.
    - All other characters are lowercase.

    In other words, Python runs:  
    `str.capitalize(my_string)`  
    or  
    `my_string[0].upper() + my_string[1:].lower()`
    (That’s not exactly how Python implements it, but that’s what it feels like!)

---

## Parameters

- There are **no parameters**.  
  You just call it on a string:  
  `some_string.capitalize()`

---

## What It Returns

- A new string with the first letter capitalized, and the rest lowercased.
- The **original string does not change** (strings are immutable in Python).

---

## Examples

- **Example 1:**  
      `"hello world".capitalize()`         # 'Hello world'

- **Example 2:**  
      `"PYTHON".capitalize()`              # 'Python'

- **Example 3:**  
      `"123abc".capitalize()`              # '123abc'   (First character isn't a letter, so just lowercases the rest)

- **Example 4:**  
      `"hElLo WoRLd!".capitalize()`        # 'Hello world!'

---

## Quick Notes

- Only the **first character** is capitalized; everything else becomes lowercase, even if it was uppercase before.
- If the first character is **not a letter** (e.g., a number or symbol), the string is lowercased after that character.
- If the string is empty, it just returns an empty string.

---

## In summary

- `capitalize()` gives you a version of your string with the first letter uppercase and all others lowercase.
- The original string isn’t changed—`capitalize()` gives you a **new** string.

---

**Tip:**  
To see more, run:

    help(str.capitalize)

---

