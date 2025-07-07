# Understanding Python’s `len()` Function: A Natural Language Explainer

When you see `len(obj)` in Python’s help system, you’re looking at the **length** function—a way to find out “how many items” are in a container (like a list, string, tuple, dictionary, etc.).

---

## What Is `len` in Python?

- `len` is a built-in function that returns the number of items in an object.
- Works with sequences (lists, tuples, strings) and collections (sets, dictionaries, etc.).

---

## What You Write and What Python Does

- **What you write:**  
    `len(obj)`

- **What Python does:**  
    Looks at the object you gave it and tries to call a special method named `__len__` on that object.  
    In other words, Python actually runs:  
    `obj.__len__()`

    - This means any object that wants to work with `len()` must have a `__len__` method defined.
    - Most built-in Python container types (lists, tuples, dicts, sets, strings, etc.) have this method already.

---

## Parameters

- `obj`: The object whose length (number of items) you want to find.
    - Must be a container with a defined length.

---

## What It Returns

- The number of items (an integer) in the container object.
- If you try to use `len()` on something that isn’t a container or doesn’t have a `__len__` method, Python will give you a `TypeError`.

---

## Examples

- **List:**  
      `len([1, 2, 3, 4])`         # 4

- **String:**  
      `len("hello")`              # 5

- **Tuple:**  
      `len((10, 20))`             # 2

- **Dictionary:**  
      `len({'a': 1, 'b': 2})`     # 2

- **Set:**  
      `len({100, 200, 300})`      # 3

---

## Custom Class Example: Making len() Work with Your Own Objects

If you want `len()` to work on your own class, define a `__len__` method:

    class Box:
        def __init__(self, items):
            self.items = items
        def __len__(self):
            return len(self.items)

    b = Box([1, 2, 3])
    len(b)      # Python calls b.__len__(), returns 3

---

## In summary

- `len()` gives you the number of items in a container.
- Under the hood, Python calls the object’s `__len__` method.
- Works with all standard containers and any custom object that defines `__len__`.

---

**Tip:**  
To see more, run:

    help(len)

---
