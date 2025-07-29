# How to Populate an Empty List Using a For Loop in Python

Populating (filling) a list with values as you go is a fundamental Python technique, especially when you want to build up data step by step.  
You typically start with an **empty list**, then use a `for` loop to add items using the `.append()` method.

---

## Step-by-Step: Populating an Empty List

1. **Create an empty list:**  
   Use `my_list = []` to make an empty list.

2. **Loop over your data:**  
   Use a `for` loop to iterate over a range, another list, or any sequence.

3. **Add values to the list:**  
   Use `my_list.append(item)` inside the loop.

---

## Example 1: Populate a List with Squares of Numbers

      squares = []
      for i in range(5):
          squares.append(i ** 2)
      print(squares)
      # Output: [0, 1, 4, 9, 16]

- `squares = []` starts you off with an empty list.
- `for i in range(5):` loops over 0, 1, 2, 3, 4.
- `squares.append(i ** 2)` adds the square of each number to the list.

---

## Example 2: Build a List from Another List

      names = ["Alice", "Bob", "Charlie"]
      name_lengths = []
      for name in names:
          name_lengths.append(len(name))
      print(name_lengths)
      # Output: [5, 3, 7]

---

## Key Points

- **Always initialize your list before the loop** (otherwise you’ll get an error).
- `.append()` adds each item to the end of the list.
- You can use `for` loops with `range()`, lists, strings, or anything you can iterate over.

---

**Summary:**  
To fill a list with values, start with `my_list = []`, then use a `for` loop with `my_list.append(item)` to add each value you want.
