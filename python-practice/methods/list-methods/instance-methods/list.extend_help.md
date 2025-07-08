# Understanding Python’s `list.extend` Method: A Natural Language Explainer

When you see `list.extend` in Python’s help system, you’re looking at the method that **adds multiple elements** from another iterable to the end of a list—in place.

---

## What Is `extend` in Python for Lists?

- `extend` is an **instance method** of the `list` type.
- It **adds each element** from the given iterable (like another list, tuple, or string) to the **end of the list**.
- The original list is **changed in place** (mutated); no new list is returned.

---

## What You Write and What Python Does

- **What you write:**  
    `[1, 2, 3].extend([4, 5])`

- **What Python does:**  
    Takes each item from the iterable and appends it to the end of the list, one by one.  
    - Under the hood, Python runs:  
      `my_list.extend(iterable)`

---

## Parameters

- ``iterable``: Any object you can loop over (list, tuple, string, set, etc.).

---

## What It Returns

- **Returns `None`.**
- The original list is **extended** (mutated) with the new elements.

---

## Examples

- **Extend with another list:**  
      `lst = [1, 2, 3]`  
      `lst.extend([4, 5])`  
      `print(lst)`             # [1, 2, 3, 4, 5]

- **Extend with a tuple:**  
      `lst = [1, 2]`  
      `lst.extend((3, 4))`  
      `print(lst)`             # [1, 2, 3, 4]

- **Extend with a string (adds each character):**  
      `lst = [1, 2]`  
      `lst.extend("ab")`  
      `print(lst)`             # [1, 2, 'a', 'b']

- **Assigning the result (DON'T DO THIS!):**  
      `lst = [1, 2]`  
      `result = lst.extend([3, 4])`  
      `print(result)`          # None  
      `print(lst)`             # [1, 2, 3, 4]

---

## Quick Notes

- This method **mutates** the original list and returns `None`.
- Each element of the iterable is added individually (not as a sublist).

---

## In summary

- `list.extend(iterable)` adds all elements from `iterable` to the end of the list.
- The original list is changed (mutated); nothing is returned.

---

**Tip:**  
To see more, run:

    help(list.extend)

---
