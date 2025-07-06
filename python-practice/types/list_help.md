# Understanding Python’s `list` Type: A Natural Language Explainer

A `list` in Python is a built-in, **mutable** sequence used to store a collection of items in a specific order.
Lists can hold any mix of objects—numbers, strings, other lists, etc.

---

## Creating a List

- **No argument:**  
        mylist = list()
        # or, using brackets:
        mylist = []

- **From an iterable (like a string, tuple, or another list):**
        chars = list("cat")        # ['c', 'a', 't']
        nums = list((1, 2, 3))    # [1, 2, 3]

---

## Special Methods (“Dunder Methods”)

Below are explanations of list special methods, including what you usually write, what Python does behind the scenes, and what each means.

---

### __add__(self, value)

- **User code:**
        newlist = [1, 2] + [3, 4]
- **Python does:**
        newlist = [1, 2].__add__([3, 4])
- **Meaning:**  
  Concatenates two lists to make a new one.
- **Example:**  
        [1, 2] + [3, 4]   # [1, 2, 3, 4]

---

### __contains__(self, key)

- **User code:**
        2 in [1, 2, 3]
- **Python does:**
        [1, 2, 3].__contains__(2)
- **Meaning:**  
  Checks if an item is in the list.
- **Example:**  
        "cat" in ["dog", "cat", "rat"]   # True

---

### __delitem__(self, key)

- **User code:**
        del mylist[0]
- **Python does:**
        mylist.__delitem__(0)
- **Meaning:**  
  Removes an item from the list at a specific index.
- **Example:**  
        a = [1, 2, 3]
        del a[1]      # a is now [1, 3]

---

### __eq__(self, value)

- **User code:**
        [1, 2] == [1, 2]
- **Python does:**
        [1, 2].__eq__([1, 2])
- **Meaning:**  
  Checks if two lists are exactly equal (same items, same order).
- **Example:**  
        [1, 2] == [1, 2]      # True
        [1, 2] == [2, 1]      # False

---

### __ge__(self, value)

- **User code:**
        [2, 3] >= [1, 4]
- **Python does:**
        [2, 3].__ge__([1, 4])
- **Meaning:**  
  Compares two lists, element by element, for greater-than-or-equal (like alphabetical order).
- **Example:**  
        [2, 3] >= [2, 3]      # True
        [3] >= [2, 9]         # True

---

### __getattribute__(self, name)

- **User code:**
        mylist.append
- **Python does:**
        mylist.__getattribute__('append')
- **Meaning:**  
  Internal method for getting an attribute or method of the list (rarely needed directly).
- **Example:**  
        a = [1]
        f = a.__getattribute__('append')
        f(2)    # a is now [1, 2]

---

### __getitem__(self, index)

- **User code:**
        item = mylist[0]
- **Python does:**
        mylist.__getitem__(0)
- **Meaning:**  
  Accesses an item by its position (index) in the list.
- **Example:**  
        a = [10, 20, 30]
        a[1]         # 20

---

### __gt__(self, value)

- **User code:**
        [2, 3] > [1, 4]
- **Python does:**
        [2, 3].__gt__([1, 4])
- **Meaning:**  
  Compares lists element by element for “greater than.”
- **Example:**  
        [2, 3] > [2, 1]    # True

---

### __iadd__(self, value)

- **User code:**
        a = [1, 2]
        a += [3, 4]
- **Python does:**
        a.__iadd__([3, 4])
- **Meaning:**  
  Adds the items from another list to this list (in-place).
- **Example:**  
        b = [5]
        b += [6, 7]   # b is now [5, 6, 7]

---

### __imul__(self, value)

- **User code:**
        a = [1, 2]
        a *= 2
- **Python does:**
        a.__imul__(2)
- **Meaning:**  
  Repeats the list in-place.
- **Example:**  
        c = [0]
        c *= 4     # c is now [0, 0, 0, 0]

---

### __init__(self, *args, **kwargs)

- **User code:**
        a = list([1, 2])
- **Python does:**
        a.__init__([1, 2])
- **Meaning:**  
  Initializes a list. Not called directly—use list() or [].

---

### __iter__(self)

- **User code:**
        for x in [1, 2, 3]: print(x)
- **Python does:**
        [1, 2, 3].__iter__()
- **Meaning:**  
  Lets you loop over the list.
- **Example:**  
        for item in [10, 20]:
            print(item)

---

### __le__(self, value)

- **User code:**
        [1, 2] <= [2, 2]
- **Python does:**
        [1, 2].__le__([2, 2])
- **Meaning:**  
  Element-wise less-than-or-equal-to comparison.
- **Example:**  
        [1, 2] <= [1, 2]  # True

---

### __len__(self)

- **User code:**
        len([1, 2, 3])
- **Python does:**
        [1, 2, 3].__len__()
- **Meaning:**  
  Returns the number of items in the list.
- **Example:**  
        len([0, 1])   # 2

---

### __lt__(self, value)

- **User code:**
        [1, 2] < [2, 2]
- **Python does:**
        [1, 2].__lt__([2, 2])
- **Meaning:**  
  Element-wise less-than comparison.
- **Example:**  
        [1, 2] < [2, 2]  # True

---

### __mul__(self, value)

- **User code:**
        [1, 2] * 3
- **Python does:**
        [1, 2].__mul__(3)
- **Meaning:**  
  Returns a new list repeated N times.
- **Example:**  
        [1, 2] * 2    # [1, 2, 1, 2]

---

### __ne__(self, value)

- **User code:**
        [1, 2] != [2, 1]
- **Python does:**
        [1, 2].__ne__([2, 1])
- **Meaning:**  
  Checks if lists are not equal.
- **Example:**  
        [1] != [2]    # True

---

### __repr__(self)

- **User code:**
        repr([1, 2])
- **Python does:**
        [1, 2].__repr__()
- **Meaning:**  
  Returns a string that looks like how you would type the list in Python.
- **Example:**  
        repr([1, 2])    # '[1, 2]'

---

### __reversed__(self)

- **User code:**
        for x in reversed([1, 2, 3]): print(x)
- **Python does:**
        [1, 2, 3].__reversed__()
- **Meaning:**  
  Returns an iterator to loop over the list backwards.
- **Example:**  
        for y in reversed([3, 1, 4]):
            print(y)

---

### __rmul__(self, value)

- **User code:**
        3 * [0]
- **Python does:**
        [0].__rmul__(3)
- **Meaning:**  
  Allows the number to be on the left in repeated lists.
- **Example:**  
        2 * [7, 8]   # [7, 8, 7, 8]

---

### __setitem__(self, key, value)

- **User code:**
        mylist[1] = 99
- **Python does:**
        mylist.__setitem__(1, 99)
- **Meaning:**  
  Changes the value at a certain index.
- **Example:**  
        x = [1, 2, 3]
        x[0] = 10   # x is now [10, 2, 3]

---

### __sizeof__(self)

- **User code:**
        [1, 2].__sizeof__()
- **Meaning:**  
  Returns the memory size of the list in bytes.

---

## Common List Methods

### append(object)

- **User code:**
        mylist.append(5)
- **Meaning:**  
  Adds an item to the end.
- **Example:**  
        a = [1, 2]
        a.append(3)    # [1, 2, 3]

---

### clear()

- **User code:**
        mylist.clear()
- **Meaning:**  
  Removes all items.
- **Example:**  
        a = [1, 2]
        a.clear()    # []

---

### copy()

- **User code:**
        newlist = oldlist.copy()
- **Meaning:**  
  Returns a shallow copy of the list.
- **Example:**  
        x = [1, 2]
        y = x.copy()
        # y == [1, 2], but x and y are different objects

---

### count(value)

- **User code:**
        [1, 2, 2].count(2)
- **Meaning:**  
  Counts how many times a value appears.
- **Example:**  
        [2, 2, 2, 1].count(2)   # 3

---

### extend(iterable)

- **User code:**
        a = [1]
        a.extend([2, 3])
- **Meaning:**  
  Adds each item from the iterable to the end.
- **Example:**  
        [1].extend([2, 3])   # [1, 2, 3]

---

### index(value, start=0, stop=len(list))

- **User code:**
        [1, 2, 3, 2].index(2)
- **Meaning:**  
  Finds the first index where a value appears.
- **Example:**  
        [3, 4, 5].index(4)   # 1

---

### insert(index, object)

- **User code:**
        a.insert(1, "hello")
- **Meaning:**  
  Inserts an item before the given position.
- **Example:**  
        l = [1, 2]
        l.insert(1, "X")   # [1, "X", 2]

---

### pop(index=-1)

- **User code:**
        val = mylist.pop()
- **Meaning:**  
  Removes and returns the item at index (last by default).
- **Example:**  
        x = [1, 2, 3]
        y = x.pop()    # y=3, x=[1,2]

---

### remove(value)

- **User code:**
        mylist.remove(2)
- **Meaning:**  
  Removes the first occurrence of the value.
- **Example:**  
        a = [1, 2, 2]
        a.remove(2)   # a is now [1, 2]

---

### reverse()

- **User code:**
        a.reverse()
- **Meaning:**  
  Reverses the list *in place*.
- **Example:**  
        nums = [1, 2, 3]
        nums.reverse()   # [3, 2, 1]

---

### sort(key=None, reverse=False)

- **User code:**
        a.sort()
- **Meaning:**  
  Sorts the list in place.
- **Example:**  
        nums = [3, 1, 2]
        nums.sort()   # [1, 2, 3]
        words = ["b", "a"]
        words.sort(reverse=True)   # ['b', 'a'] becomes ['b', 'a']

---

## Summary

- Lists are Python’s “workhorse” for ordered collections of items.
- Use `[]` to create, access, change, and manipulate them.
- Methods let you append, remove, sort, and do much more.

---

