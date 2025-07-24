# Understanding Loops in Python: A Natural Language Explainer

Loops let you **repeat actions multiple times** in your code—perfect for working with lists, processing data, or automating repetitive tasks. In Python, the two main types of loops are the `for` loop and the `while` loop.

---

## What Is a Loop?

- A **loop** is a way to run a block of code several times.
- Each “round” through the loop is called an **iteration**.
- Loops help you avoid copy-pasting the same code over and over.

---

## The `for` Loop

- **Use when you want to loop over each item in a sequence** (like a list, string, tuple, etc.).
- Syntax:
  
      for item in sequence:
          # do something with item

- On each loop, `item` takes the next value from `sequence`.

---

### Examples

- **Loop over a list:**

      for num in [1, 2, 3]:
          print(num)    # Prints 1, then 2, then 3

- **Loop over a string:**

      for letter in "hi":
          print(letter) # Prints 'h', then 'i'

---

## The `while` Loop

- **Use when you want to repeat something as long as a condition is true.**
- Syntax:

      while condition:
          # do something

- Python checks the `condition` before each loop—if it’s `True`, the block runs again.

---

### Example

- **Count down from 3 to 1:**

      n = 3
      while n > 0:
          print(n)
          n = n - 1
      # Prints 3, then 2, then 1

---

## Breaking Out of Loops

- **`break`**: Stop the loop immediately.

      for i in range(5):
          if i == 3:
              break   # Stops loop when i is 3
          print(i)

- **`continue`**: Skip to the next iteration.

      for i in range(5):
          if i == 2:
              continue  # Skips printing 2
          print(i)

---

## Looping with `range()`

- `range()` lets you loop a set number of times.

      for i in range(5):   # Loops 0, 1, 2, 3, 4 (not 5)
          print(i)

---

## In Summary

- **Use `for` loops** to process each item in a collection.
- **Use `while` loops** when you don’t know in advance how many times you’ll need to repeat.
- Loops help you write less code and automate repetitive tasks.
- Control loops with `break` (to exit) and `continue` (to skip to the next round).

---

**Tip:**   
Try writing your own loops! Loops are everywhere in Python—from data analysis to web development.