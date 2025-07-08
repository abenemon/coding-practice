# Understanding Python’s `list.sort` Method: A Natural Language Explainer

When you see `list.sort` in Python’s help system, you’re looking at the method that **sorts the items** of a list—in place.

---

## What Is `sort` in Python for Lists?

- `sort` is an **instance method** of the `list` type.
- It **sorts the elements** of the list **in place**, in ascending order by default.
- The original list is changed (mutated); no new list is returned.
- The sort is **stable**: items with equal values keep their original order.

---

## What You Write and What Python Does

- **What you write:**  
    `[3, 1, 2].sort()`

- **What Python does:**  
    Reorders the elements of the list from lowest to highest (or as specified), **changing the original list**.  
    - Under the hood, Python runs:  
      `my_list.sort(key=None, reverse=False)`

---

## Parameters

- ``key`` (optional): A function that takes one argument and returns a value to use for sorting.
- ``reverse`` (optional): Boolean; if `True`, sort in descending order.

---

## What It Returns

- **Returns `None`.**
- The original list is **sorted in place** (mutated).

---

## Examples

- **Sort numbers in ascending order:**  
      `lst = [3, 1, 2]`  
      `lst.sort()`  
      `print(lst)`                 # [1, 2, 3]

- **Sort in descending order:**  
      `lst = [3, 1, 2]`  
      `lst.sort(reverse=True)`  
      `print(lst)`                 # [3, 2, 1]

- **Sort with a key function:**  
      `lst = ["apple", "banana", "pear"]`  
      `lst.sort(key=len)`  
      `print(lst)`                 # ['pear', 'apple', 'banana'] (shortest to longest)

- **Assigning the result (DON'T DO THIS!):**  
      `lst = [3, 2, 1]`  
      `result = lst.sort()`  
      `print(result)`              # None  
      `print(lst)`                 # [1, 2, 3]

---

## Quick Notes

- This method **mutates** the original list and returns `None`.
- If you want a **sorted copy** of a list without changing the original, use the built-in `sorted()` function:
      `new_list = sorted(lst)`

---

## In summary

- `list.sort()` sorts the list in place (mutates the list) and returns `None`.
- Use the `key` parameter for custom sorting.
- Use `reverse=True` for descending order.

---

**Tip:**  
To see more, run:

    help(list.sort)

---
