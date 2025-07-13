Placehold# Understanding NumPy’s Array Type: The `ndarray`

In NumPy, the main type for storing and working with data is the `ndarray`—short for “N-dimensional array.” Almost everything in NumPy starts with, or returns, an `ndarray`!

---

## What is an `ndarray`?

- `ndarray` stands for **N-dimensional array**.
- It is the core data structure of NumPy, storing elements of the same type in a regular grid (1D, 2D, 3D, or more!).
- Every array you create with `np.array()`, `np.zeros()`, `np.ones()`, etc., is actually an instance of `numpy.ndarray`.

---

## How Do You Create an `ndarray`?

- Use functions like `np.array()`, `np.arange()`, `np.zeros()`, `np.ones()`, `np.linspace()`, or others.
- Example:
  - `a = np.array([1, 2, 3])` → `a` is a 1D `ndarray`.
  - `b = np.array([[1, 2], [3, 4]])` → `b` is a 2D `ndarray`.

---

## Key Attributes of an `ndarray`

- `.shape`: The size of the array in each dimension (as a tuple).
  - Example: `a.shape` → `(3,)` for a 1D array with 3 elements.
- `.dtype`: The type of elements in the array (like `int32`, `float64`).
  - Example: `a.dtype` → `dtype('int64')` if you made an integer array.
- `.ndim`: The number of dimensions (axes) in the array.
  - Example: `b.ndim` → `2` for a 2D array.
- `.size`: The total number of elements.
  - Example: `b.size` → `4` for a 2x2 array.

---

## Why Use an `ndarray` Instead of a List?

- Faster for numeric operations (vectorized math, broadcasting).
- Uses less memory for large numeric data.
- Offers a huge collection of methods and NumPy functions that work efficiently on arrays (`sum()`, `mean()`, `reshape()`, etc.).
- Supports multi-dimensional data (lists only do 1D directly).

---

## How Do You Check if Something is an `ndarray`?

- Use `type(x)` or `isinstance(x, np.ndarray)`.
  - Example:  
    `import numpy as np`  
    `a = np.array([1, 2, 3])`  
    `type(a)` → `<class 'numpy.ndarray'>`  
    `isinstance(a, np.ndarray)` → `True`

---

## Example Usage

- **Create an array:**  
  `a = np.array([10, 20, 30])`
- **Check the type:**  
  `type(a)` → `<class 'numpy.ndarray'>`
- **Access attributes:**  
  `a.shape` → `(3,)`  
  `a.dtype` → `dtype('int64')`  
  `a.ndim` → `1`  
  `a.size` → `3`
- **Use array methods:**  
  `a.sum()` → `60`  
  `a.mean()` → `20.0`  
  `a.reshape((3, 1))` → reshapes `a` to a column vector

---

## A Note About Mutability

- `ndarray` objects are **mutable**—you can change their elements after creation.
  - Example:  
    `a[0] = 99` changes the first element of `a` to `99`.

---

## In summary

- The `ndarray` is the heart of NumPy.
- It stores data in N dimensions, offers efficient math, and provides attributes for shape, type, and more.
- All serious work in NumPy is done with arrays of this type.

---

**Tip:**  
Use `help(np.ndarray)` or `dir(np.ndarray)` to see all available methods and attributes.

---
er
