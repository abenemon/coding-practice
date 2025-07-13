# NumPy 2D Arrays: What They Are and How to Create Them

A **NumPy 2D array** is a grid of numbers with rows and columns, like a table or a matrix. In NumPy, these are called `ndarray` objects with two dimensions.

---

## What Is a 2D Array?

- A 2D array is a rectangular arrangement of numbers, with rows and columns.
- Each value is accessed with two indices: `array[row, column]`.
- Example: a 3x2 array (3 rows, 2 columns):

    `[[1, 2],`
     `[3, 4],`
     `[5, 6]]`

- The shape of this array is `(3, 2)`.

---

## Why Use NumPy 2D Arrays?

- They are much faster and more memory-efficient than regular Python lists of lists.
- You can do math on whole arrays at once (element-wise).
- They’re essential for scientific computing, data analysis, and machine learning.

---

## How to Create a 2D Array

1. **From a list of lists:**

    ```python
    import numpy as np
    arr = np.array([[1, 2, 3],
                    [4, 5, 6]])
    ```
    This creates a 2D array with shape `(2, 3)` (2 rows, 3 columns).

2. **Using NumPy functions:**

    ```python
    np.zeros((3, 2))      # 3 rows, 2 columns, all zeros
    np.ones((2, 4))       # 2 rows, 4 columns, all ones
    np.random.rand(3, 3)  # 3x3 array with random values
    np.eye(3)             # 3x3 identity matrix
    ```

3. **Reshaping a 1D array:**

    ```python
    a = np.arange(6)        # array([0, 1, 2, 3, 4, 5])
    b = a.reshape((2, 3))   # shape (2, 3)
    ```

---

## Accessing Elements

- Element at row 1, column 2: `arr[1, 2]`
- First row: `arr[0]`
- Second column: `arr[:, 1]`

---

## In Summary

- A NumPy 2D array is a table of values, efficient and powerful for data work.
- Make one from a list of lists, or with functions like `np.zeros`, `np.ones`, or by reshaping.
- Use `arr.shape` to check the size: returns `(rows, columns)`.

---
