# Understanding Python’s `list.reverse` Method: A Natural Language Explainer

When you see `list.reverse` in Python’s help system, you’re looking at the method that **reverses the order** of elements in a list—in place.

---

## What Is `reverse` in Python for Lists?

- `reverse` is an **instance method** of the `list` type.
- It **reverses the elements** of the list **in place**.
- The list is **changed**; no new list is returned.

---

## What You Write and What Python Does

- **What you write:**  
    `[1, 2, 3].reverse()`

- **What Python does:**  
    Changes the original list so that its elements appear in the opposite order.  
    - Under the hood, Python runs:  
      `my_list.reverse()`

---

## Parameters

- None (other than `self`, the list itself).

---

## What It Returns

- **Returns `None`.**
- The original list is **reversed in place** (mutated).

---

## Examples

- **Reverse a list of numbers:**  
      `lst = [1, 2, 3]`  
      `lst.reverse()`  
      `print(lst)`               # [3, 2, 1]

- **Reverse a list of strings:**  
      `lst = ['a', 'b', 'c']`  
      `lst.reverse()`  
      `print(lst)`               # ['c', 'b', 'a']

- **Assigning the result (DON'T DO THIS!):**  
      `lst = [1, 2, 3]`  
      `result = lst.reverse()`  
      `print(result)`            # None  
      `print(lst)`               # [3, 2, 1]

---

## Quick Notes

- This method **mutates** the original list and returns `None`.
- If you want a reversed version of the list **without changing the original**, use slicing:  
      `reversed_lst = lst[::-1]`

---

## In summary

- `list.reverse()` reverses the list in place.
- The original list is changed; nothing is returned.

---

**Tip:**  
To see more, run:

    help(list.reverse)

---
