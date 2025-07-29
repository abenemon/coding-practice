# Understanding `np.random.randint`: Generating Random Integers in NumPy

The `np.random.randint` function in NumPy generates random **integers** from a specified range.  
It’s the go-to way to create arrays or single values of random whole numbers for simulations, sampling, or test data.

---

## What Is `np.random.randint`?

- A function in NumPy’s `random` module.
- Produces random integers from a given lower bound (inclusive) up to an upper bound (exclusive).

---

## Syntax

    np.random.randint(low, high=None, size=None, dtype=int)

- `low`: **Required**. The lowest integer to be drawn from (inclusive).
- `high`: **Optional**. The highest integer to be drawn from (exclusive). If not specified, integers are drawn from `0` to `low` (exclusive).
- `size`: **Optional**. The shape of the output (single value, 1D array, 2D array, etc.).
- `dtype`: **Optional**. The data type of the output (default is `int`).

---

## What Does It Return?

- If `size` is `None`, returns a single integer.
- If `size` is specified, returns an array of random integers of that shape.

---

## Examples

- **Single random integer between 0 and 9:**

      import numpy as np
      np.random.randint(0, 10)
      # e.g. 7

- **Single random integer between 5 and 15:**

      np.random.randint(5, 15)
      # e.g. 12

- **1D array of 4 random integers from 0 to 99:**

      np.random.randint(0, 100, size=4)
      # e.g. array([13, 85, 2, 77])

- **2D array (3 rows, 2 columns) of random numbers from 1 to 6:**

      np.random.randint(1, 7, size=(3, 2))
      # e.g. array([[4, 2],
      #             [5, 6],
      #             [1, 3]])

---

## How It’s Different From…

- `np.random.rand`: Generates random **floats** between 0 and 1.
- `np.random.randn`: Generates random floats from a **normal distribution**.
- `np.random.choice`: Randomly selects items from a given list or array.

---

## Common Uses

- Simulating dice rolls or random events
- Creating random indices or sample data
- Randomly shuffling or assigning group labels

---

**Summary:**  
Use `np.random.randint` when you need random whole numbers in a specified range, as single values or in arrays of any shape.
