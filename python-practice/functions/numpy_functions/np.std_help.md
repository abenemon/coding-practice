# Understanding `np.std`: Standard Deviation in NumPy

The NumPy function `np.std()` computes the **standard deviation** of an array, which is a measure of how much the elements deviate from the mean. It’s a common statistic in data analysis and science.

---

## What Does `np.std` Do?

- Calculates the **spread (dispersion)** of values in an array.
- By default, computes over all elements (flattened).
- You can calculate standard deviation along any axis (per row, per column, etc).

---

## Parameters

- `a`:  
    The data (array-like or convertible to an array) to compute standard deviation on.

- `axis`: (optional)  
    The axis or axes along which to calculate.  
    - `None` (default): all elements.  
    - `0`: compute for each column (down the rows).  
    - `1`: compute for each row (across columns).

- `dtype`: (optional)  
    Type used for calculation.  
    - For integer arrays, default is `float64`.
    - For float arrays, uses input type.

- `out`: (optional)  
    Alternate array to write results into.

- `ddof`: (optional, default `0`)  
    Delta Degrees of Freedom. Divisor is `N - ddof` (where `N` is number of elements).  
    - Use `ddof=0` for **population standard deviation** (default).
    - Use `ddof=1` for **sample standard deviation** (with Bessel's correction).

- `keepdims`: (optional)  
    If `True`, reduced axes are kept as dimensions with size one, making broadcasting easier.

- `where`: (optional)  
    Boolean mask: only compute standard deviation over elements where `where=True`.

- `mean`: (optional, new in NumPy 2.0)  
    Pre-computed mean. Pass this if you already have the mean and want to save computation time.

- `correction`: (optional, new in NumPy 2.0)  
    Synonym for `ddof` (use one or the other).

---

## What Does It Return?

- An array (or scalar) with the **standard deviation** of the input.
- The result’s shape depends on the `axis` argument.

---

## Standard Deviation Formula Used

If `a` is a 1D array and `mean` is the mean of `a`:

    N = len(a)
    var = sum(abs(a - mean)**2) / (N - ddof)
    std = sqrt(var)

---

## Example Usage

    import numpy as np

    a = np.array([[1, 2], [3, 4]])

    # Standard deviation of all elements
    np.std(a)              # 1.118...

    # By column (axis=0)
    np.std(a, axis=0)      # array([1., 1.])

    # By row (axis=1)
    np.std(a, axis=1)      # array([0.5, 0.5])

---

## Sample vs Population Standard Deviation

By default, `np.std` divides by `N` (`ddof=0`) — this is the **population standard deviation**.

If you want the **sample standard deviation** (more common in statistics), use `ddof=1`:

    np.std(a, ddof=1)

This divides by `N - 1` (Bessel's correction).

---

## Advanced Features

- **Single-precision can be imprecise:**  
    Use `dtype=np.float64` for better accuracy on large arrays of float32.

- **Using `where` to select elements:**  
    a = np.array([[14, 8, 11, 10], [7, 9, 10, 11], [10, 15, 5, 10]])
    np.std(a, where=[[True], [True], [False]])  # 2.0

- **Saving time by providing the mean:**  
    mean = np.mean(a, axis=1, keepdims=True)
    np.std(a, axis=1, mean=mean)

---

## Summary

- `np.std` gives you a quick way to compute standard deviation for arrays, rows, columns, or masked data.
- Default is population std. Use `ddof=1` for sample std.
- For best precision, use `dtype` or precompute the mean if you're calling it repeatedly.
- The standard deviation always returns real, nonnegative results—even for complex input.

---

**Tip:**  
If you want the **variance** (std squared), use `np.var`.  
For ignoring NaN values, see `np.nanstd`.

