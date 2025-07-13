# Understanding `np.shape`: Finding the Shape of Arrays

The function `np.shape` in NumPy returns the shape of an array—that is, it tells you the size of each dimension (axis) of your data structure.

---

## What Does `np.shape` Do?

- `np.shape(a)` returns a tuple of integers describing the length of each dimension of the input `a`.
- It works on any array-like object, not just NumPy arrays—so you can use it on lists, tuples, and more.
- The length of the tuple tells you how many dimensions the array has.
- If `a` is a scalar (a single value, not a sequence), `np.shape(a)` returns an empty tuple: `()`.

---

## Parameters

- `a`: The input array or array-like object (list, tuple, etc.).

---

## What It Returns

- A tuple of integers: each integer is the size of one axis (dimension).
- Example: For a 2D array with shape 3 rows by 4 columns, `np.shape(a)` → `(3, 4)`.

---

## Examples

```python
import numpy as np

np.shape(np.eye(3))        # (3, 3)   -- 3x3 identity matrix
np.shape([[1, 3]])         # (1, 2)   -- 1 row, 2 columns (list of list)
np.shape([0])              # (1,)     -- 1D array of length 1
np.shape(0)                # ()       -- Scalar, no shape

# Works with structured arrays too:
a = np.array([(1, 2), (3, 4), (5, 6)], dtype=[('x', 'i4'), ('y', 'i4')])
np.shape(a)                # (3,)
a.shape                    # (3,)     -- Equivalent attribute
