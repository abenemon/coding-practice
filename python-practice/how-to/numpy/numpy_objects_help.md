# Using `help()` on NumPy Functions and Understanding NumPy Object Types

You can use Python’s built-in `help()` function on most NumPy functions, classes, and even many NumPy objects, just like you can with standard Python. This is a great way to get detailed documentation, including parameters, usage, and examples.

---

## Can You Call `help()` on NumPy Functions and Classes?

- **Yes!**  
  You can use `help()` on NumPy functions (like `np.array`), classes (like `np.ndarray`), methods (like `a.reshape`), and even the whole NumPy module (`np`).

- **How?**  
  Write something like `help(np.array)` or `help(np.mean)` after you `import numpy as np`.

- **Tip:**  
  In Jupyter or IPython, you can also write `np.mean?` or `np.mean??` to see the docstring.

---

## What Object Types Exist in NumPy? Are They the Same as Python’s?

NumPy extends standard Python with special types for efficient numeric computation. Here are some key object types you’ll encounter:

- **`ndarray`**  
  The core type: a multi-dimensional, fixed-type array of values.  
  Example: `a = np.array([1, 2, 3])` gives you an object of type `numpy.ndarray`.

- **`dtype`**  
  Describes the data type of the array’s elements (like `int32`, `float64`, etc.).  
  Example: `a.dtype` might be `dtype('int64')`.

- **Universal functions (`ufunc`)**  
  Special vectorized functions that work elementwise on arrays (like `np.add`, `np.sin`).  
  Example: `type(np.add)` is `numpy.ufunc`.

- **NumPy scalars**  
  Types like `np.int32`, `np.float64`, etc. These are similar to Python’s built-in `int` and `float`, but with specific precision and behavior.

- **Masked arrays and matrices**  
  Less common, but available: `np.ma.MaskedArray` (for data with missing values), and `np.matrix` (an older matrix type—generally, use `ndarray` instead).

**Are they the same as Python’s built-in types?**  
- No. NumPy types are optimized for arrays and numeric work.  
- A NumPy array (`ndarray`) is not a Python `list`, and NumPy’s scalar types (like `np.float32`) are not exactly the same as Python’s `float`.
- They work together, but NumPy types give you speed, precision, and features needed for scientific computing.

---

## Using `help()` on NumPy Objects: Example

After running `import numpy as np`, try:

- `help(np.array)`  
  Shows details for the array creation function.
- `help(np.mean)`  
  Shows how to compute the mean of an array.
- `help(np.ndarray)`  
  Shows info for the array object itself.
- `help(a.reshape)`  
  If `a` is an array, this gives help for the reshape method.
- `help(np)`  
  Overview of the NumPy module.

**Example session:**
- `import numpy as np`
- `help(np.array)`

This brings up a detailed description, including:

- **Signature:**  
  `array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)`
- **Parameters:**  
  - `object`: Input data (list, tuple, etc.).
  - `dtype`: Desired data-type.
  - `copy`: Whether to copy the data.
  - `order`: Memory layout order.
  - `subok`: If subclasses are allowed.
  - `ndmin`: Minimum number of dimensions.
  - `like`: (Advanced use) array-like reference object.
- **Returns:**  
  `ndarray`: The created array.
- **Examples:**  
  - `np.array([1, 2, 3])` returns an array with values `[1, 2, 3]`.
  - `np.array([[1, 2], [3, 4]])` returns a 2D array.
  - `np.array([1, 2, 3], dtype=float)` returns a float array.
  - `np.array([1, 2, 3], ndmin=2)` returns a 2D array with shape `(1, 3)`.

---

## In summary

- You **can** call `help()` on most things in NumPy—functions, classes, methods, and the whole module.
- NumPy introduces its own types (like `ndarray`, `dtype`, and `ufunc`), which are not the same as Python’s built-ins, but work alongside them.
- `help()` will show you function signatures, parameter explanations, and usage examples—just like it does for standard Python objects.

---

**Tip:**  
To see more, run `help(np.array)` or try `np.array?` in Jupyter/IPython.

---
