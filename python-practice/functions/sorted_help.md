# Understanding Python’s `sorted()` Function: A Natural Language Explainer

When you see `sorted(iterable, /, *, key=None, reverse=False)` in Python’s help system, you’re looking at the **sorted** function—a way to make a new, sorted list from any group of items.

---

## What Is `sorted` in Python?

- `sorted` is a built-in function that takes any iterable (like a list, tuple, string, set, or dictionary keys) and returns a **new list** with all the items in ascending order (by default).
- It does **not** change the original iterable—your data stays as it was.
- You can control how items are sorted with a `key` function, and whether the sort is in reverse order.

---

## What You Write and What Python Does

- **What you write:**  
    `sorted(iterable)`  
    `sorted(iterable, key=some_function, reverse=True)`

- **What Python does:**  
    Python makes a list from all the items in your iterable and sorts them.
    By default, it compares items using their built-in comparison dunder methods (`__lt__`, “less than”), just like how `max()` works.
    - If you give a `key` function, Python uses it to extract a “sort value” from each item.
    - If you set `reverse=True`, the list is sorted in descending order.

    There is **no special `__sorted__` method**; all sorting uses the comparison dunder methods on the objects themselves.

---

## Parameters

- `iterable`: The collection you want to sort (list, tuple, string, set, dictionary keys, etc.).
- `key` (optional): A function that takes an item and returns a value to sort by.
    - Example: `key=str.lower` to sort strings without case-sensitivity.
- `reverse` (optional): If `True`, sorts in descending order (largest first). Default is `False`.

---

## What It Returns

- Always returns a **new list** with the sorted items.  
  (The original is untouched.)

---

## Examples

- **Sort a list of numbers:**  
      `sorted([3, 1, 4, 2])`             # [1, 2, 3, 4]

- **Sort in reverse order:**  
      `sorted([3, 1, 4, 2], reverse=True)`   # [4, 3, 2, 1]

- **Sort a string’s letters:**  
      `sorted("cab")`                    # ['a', 'b', 'c']

- **Sort by string length:**  
      `words = ["pear", "apple", "banana"]`  
      `sorted(words, key=len)`           # ['pear', 'apple', 'banana']

- **Sort ignoring case:**  
      `names = ["alice", "Bob", "carol"]`  
      `sorted(names, key=str.lower)`     # ['alice', 'Bob', 'carol']

---

## How Does It Work for Custom Classes?

To make `sorted()` work with your own objects, define comparison methods (like `__lt__`) in your class.  
Or, supply a `key` function that returns something sortable for each object.

    class Fruit:
        def __init__(self, name, sweetness):
            self.name = name
            self.sweetness = sweetness
        def __lt__(self, other):
            return self.sweetness < other.sweetness

    fruits = [Fruit("apple", 5), Fruit("banana", 7), Fruit("lemon", 3)]
    sorted_fruits = sorted(fruits)  # sorts by sweetness

---

## In summary

- `sorted()` makes a new, sorted list from any iterable.
- You can control sorting with the `key` function and `reverse` flag.
- Sorting uses objects’ comparison methods (`__lt__`, etc.), not a `__sorted__` method.
- Original data is never changed.

---

**Tip:**  
To see more, run:

    help(sorted)

---
