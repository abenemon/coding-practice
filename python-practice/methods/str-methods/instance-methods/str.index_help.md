# Understanding Python’s `str.index` Method: A Natural Language Explainer

When you see `str.index` in Python’s help system, you’re looking at the method that tells you **where** a substring first appears in a string (or if it does at all).

---

## What Is `index` in Python for Strings?

- `index` is an **instance method** of the `str` type.
- It returns the **position** (lowest index) where a substring appears in a string.
- If the substring is **not found**, it raises a `ValueError`.

---

## What You Write and What Python Does

- **What you write:**  
    `"hello world".index("o")`

- **What Python does:**  
    Searches the string from left to right, looking for the first appearance of the substring ``sub`` within the optional range ``[start:end]``, and returns its position (as an integer).
    - Under the hood, Python runs:  
      `"hello world".index("o", start, end)`

---

## Parameters

- ``sub``: The substring you are searching for.
- ``start`` (optional): The starting index to search from (default is the beginning).
- ``end`` (optional): The ending index to search up to (default is the end of the string).

---

## What It Returns

- The **index** (integer) of the **first occurrence** of ``sub`` in the string.
- If ``sub`` is not found, Python **raises a `ValueError`** instead of returning -1.

---

## Examples

- **Find the position of a letter:**  
      `"hello world".index("o")`         # 4

- **Find the position of a substring:**  
      `"hello world".index("world")`     # 6

- **Specify where to start searching:**  
      `"hello world".index("o", 5)`      # 7

- **Limit the search to a slice:**  
      `"hello world".index("o", 5, 8)`   # 7

- **If substring is not found:**  
      `"hello world".index("z")`         # ValueError: substring not found

---

## Quick Notes

- **`index` vs. `find`:**  
  - `index` raises an error if not found;  
    `find` returns `-1` instead.
- **Start and end follow slice notation:**  
  - Start is inclusive, end is exclusive (just like string slices).

---

## In summary

- `str.index` tells you the position of the first occurrence of a substring.
- If the substring is not present, it raises a `ValueError`.
- To avoid errors when the substring might not be found, use `str.find` instead.

---

**Tip:**  
To see more, run:

    help(str.index)

---
