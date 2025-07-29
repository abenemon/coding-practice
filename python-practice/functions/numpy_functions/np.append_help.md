# Understanding `np.append`: Adding Values to NumPy Arrays

The `np.append` function in NumPy lets you add values to the end of an array, creating a new array that contains both the original elements and the new values.  
It's useful for building up arrays when you don't know all the data in advance—but it's not always the most efficient method for large or repeated operations.

---

## What Is `np.append`?

- A function that returns a **new array** with additional values appended to an existing array.
- Does **not** modify the original array (the operation is not "in-place").
- Works for 1D and multi-dimensional arrays.

---

## Syntax

    np.append(arr, values, axis=None)

- `arr`: The original array (any shape).
- `values`: The values to add (must match shape if using `axis`).
- `axis`: (Optional) The axis along which to append. If not specified, both `arr` and `values` are flattened before the operation.

---

## Key Points

- **A new array is always created** (original is unchanged).
- If `axis` is `None` (the default), both arrays are flattened and the result is 1D.
- If `axis` is given, `values` must match the dimensions of `arr` (excluding the axis being appended).

---

## Examples

- **Append to a 1D array (default, axis=None):**

      import numpy as np
      np.append([1, 2, 3], [4, 5, 6])
      # Output: array([1, 2, 3, 4, 5, 6])

- **Append multiple arrays (flattened):**

      np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])
      # Output: array([1, 2, 3, 4, 5, 6, 7, 8, 9])

- **Append to a 2D array along axis 0 (add a row):**

      np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis=0)
      # Output:
      # array([[1, 2, 3],
      #        [4, 5, 6],
      #        [7, 8, 9]])

- **Common mistake: wrong shape when using axis**

      np.append([[1, 2, 3], [4, 5, 6]], [7, 8, 9], axis=0)
      # ValueError: shapes must match; both must be 2D arrays to append along axis 0

- **Appending an empty array returns a copy (with possible dtype change):**

      a = np.array([1, 2], dtype=int)
      c = np.append(a, [])
      # c: array([1., 2.])
      # Note: result has dtype float64 because empty arrays default to float64

---

## Performance Note

- `np.append` is **not efficient** for repeatedly building large arrays—NumPy creates a new copy each time.
- For many additions, it's better to collect items in a list, then use `np.array` or `np.stack` at the end.

---

**Summary:**  
Use `np.append` to add values to arrays, but be careful with shapes and performance for large or repeated operations.
