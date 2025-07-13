# Understanding `np.mean`: The NumPy Function for Averages

The NumPy function `np.mean()` computes the arithmetic mean (average) of a group of numbers. It's a core tool for quickly finding the average value across arrays—whether you want the mean of everything, of each row, of each column, or just certain elements.

---

## What Does `np.mean` Do?

- Calculates the **average value** of the numbers you give it.
- By default, it averages *all* elements in the input.
- You can focus the averaging on specific axes (like rows or columns), or even select certain elements with a mask.

---

## Parameters: What Goes Into `np.mean`?

Here’s what you can give to `np.mean`:

- `a`:  
    The main input. This is the **data whose mean you want to calculate**.  
    It can be:
    - A NumPy array (e.g., `np.array([[1,2],[3,4]])`)
    - A regular Python list or tuple (`[1, 2, 3]`)
    - Any “array-like” object
    - NumPy will convert whatever you pass into an array, if possible.
- `axis`: (optional)  
    Which axis (dimension) to average over.
    - `None` (default): Average over *all* values (the flattened array)
    - `0`: Average **down the rows** (per column)
    - `1`: Average **across the columns** (per row)
    - For higher dimensions, you can use a tuple of axes
- `dtype`: (optional)  
    The data type to use for the calculation (like `np.float64`). Use this to avoid loss of precision.
- `out`: (optional)  
    An array to store the result, if you want to avoid creating a new one.
- `keepdims`: (optional)  
    If `True`, the reduced axes are left in the result as dimensions with size one. This helps with broadcasting later.
- `where`: (optional, advanced)  
    A Boolean mask—**only include values where this is True**.

---

## What Does It Return?

- If you average everything, you get a single number (a scalar).
- If you use `axis`, you get an array of means along that axis.
    - Example: With a 2D array and `axis=0`, you get the mean of each column.

---

## Basic Usage

    import numpy as np

    # Averaging all elements
    a = np.array([[1, 2], [3, 4]])
    np.mean(a)         # 2.5

    # Averaging by column (axis=0)
    np.mean(a, axis=0) # array([2., 3.])

    # Averaging by row (axis=1)
    np.mean(a, axis=1) # array([1.5, 3.5])

---

## More Examples

- **With a regular Python list:**
  
      np.mean([1, 2, 3, 4])   # 2.5

- **Mean with a Boolean mask (`where`):**
  
      a = np.array([[5, 9, 13], [14, 10, 12], [11, 15, 19]])
      np.mean(a, where=[[True], [False], [False]])  # 9.0

- **Mean with higher precision:**
  
      a = np.zeros((2, 512*512), dtype=np.float32)
      a[0, :] = 1.0
      a[1, :] = 0.1
      np.mean(a)                       # May lose some accuracy due to float32
      np.mean(a, dtype=np.float64)     # More accurate (uses float64)

- **Mean of timedeltas:**
  
      b = np.array([1, 3], dtype="timedelta64[D]")
      np.mean(b)   # np.timedelta64(2,'D')

---

## How Is the Mean Calculated?

The mean is simply the **sum of all elements divided by how many there are**.

    np.mean([2, 4, 6, 8])    # (2+4+6+8)/4 = 5.0

---

## Note on Precision

- For **integer input**, NumPy automatically uses `float64` for accuracy.
- For **floating-point input**, NumPy keeps the same type (e.g., `float32` stays `float32`).  
  If you care about extra precision, use `dtype=np.float64`.
- For **very large arrays**, always consider using `dtype=np.float64` unless you’re sure about the types.

---

## In Summary

- `np.mean` calculates the average of the values you pass in, along any axis you want.
- The main input is `a`—the array or list of numbers whose mean you want.
- For advanced control, use `axis`, `dtype`, `where`, and other options.
- The return value is either a single number or an array of averages, depending on your axes.
- Great for arrays, lists, and more—no need to manually sum and divide!

---

**Tip:**  
- For weighted averages, use `np.average`.
- To ignore NaN values, use `np.nanmean`.
