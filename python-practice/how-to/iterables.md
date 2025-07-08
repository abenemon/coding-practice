# What Is an Iterable in Python? A Natural Language Explainer

## Basic Definition

- An **iterable** is *any object* in Python that you can **loop over** (iterate through) one element at a time.
- If you can use an object in a `for` loop, it’s an iterable.

---

## Common Examples of Iterables

- `list`: `[1, 2, 3]`
- `tuple`: `(1, 2, 3)`
- `str`: `"hello"`  *(iterates over characters)*
- `set`: `{1, 2, 3}`
- `dict`: `{"a": 1, "b": 2}` *(iterates over keys by default)*
- `range` objects: `range(5)`

---

## Technical Definition

- An object is **iterable** if it implements the **`__iter__()`** method (and/or the older `__getitem__()` with integer keys).
- When you do `for item in my_obj:`, Python calls `my_obj.__iter__()` to get an **iterator**.

---

## How to Check if Something Is Iterable

- You can use the built-in `iter()` function:
    ```python
    iter([1, 2, 3])      # works, returns an iterator
    iter(42)             # TypeError: 'int' object is not iterable
    ```

---

## In Practice

- You can loop over any iterable:
    ```python
    for letter in "hello":
        print(letter)
    # Prints: h e l l o
    ```

- `list.extend()` takes any iterable:
    ```python
    lst = [1, 2]
    lst.extend((3, 4))   # tuple is iterable
    lst.extend("ab")     # string is iterable
    # lst is now [1, 2, 3, 4, 'a', 'b']
    ```

---

## What’s **Not** Iterable?

- Basic numbers like `int` and `float` are **not** iterable:
    ```python
    for x in 42:
        # TypeError: 'int' object is not iterable
    ```

---

## In summary

- **Iterable** = “can be looped over.”
- Lists, tuples, strings, sets, dicts, ranges, files, and more are all iterables.
- If you want to make your own class iterable, define a `__iter__()` method.

---

**Tip:**  
If you can use it in a `for` loop, it’s an iterable!

---
