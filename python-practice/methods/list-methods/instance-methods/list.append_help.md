# Understanding Python’s `list.append` Method: A Natural Language Explainer

When you see `list.append` in Python’s help system, you’re looking at the method that **adds a new item** to the end of a list.

---

## What Is `append` in Python for Lists?

- `append` is an **instance method** of the `list` type.
- It **adds** the specified object to the **end of the list**.
- The list is **modified in place** (mutated); no new list is returned.

---

## What You Write and What Python Does

- **What you write:**  
    `[1, 2, 3].append(4)`

- **What Python does:**  
    Adds the object to the end of the list, extending its length by one.  
    - Under the hood, Python runs:  
      `my_list.append(object)`

---

## Parameters

- ``object``: The item you want to add to the end of the list.

---

## What It Returns

- **Returns `None`.**
- The original list is **changed** (mutated)—the new item is now part of the list.

---

## Examples

- **Append a number:**  
      `lst = [1, 2, 3]`  
      `lst.append(4)`  
      `print(lst)`             # [1, 2, 3, 4]

- **Append a string:**  
      `lst = ['a', 'b']`  
      `lst.append('c')`  
      `print(lst)`             # ['a', 'b', 'c']

- **Append another list (creates a nested list):**  
      `lst = [1, 2]`  
      `lst.append([3, 4])`  
      `print(lst)`             # [1, 2, [3, 4]]

---

## Quick Notes

- `append` adds the object as a **single element**—it does not flatten lists.
- This method **mutates** the original list and returns `None`.
- To add multiple elements, use `extend` instead.

---

## In summary

- `list.append(object)` adds `object` to the end of the list.
- The list is changed in place; nothing is returned.

---

**Tip:**  
To see more, run:

    help(list.append)

---
