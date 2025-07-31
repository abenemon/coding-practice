# Understanding `pd.DataFrame.agg`: A Natural Language Explainer

The `.agg()` (short for "aggregate") method in pandas lets you quickly compute one or more summary statistics—like `min`, `max`, `mean`, or even custom functions—across your DataFrame, either by columns or by rows.

---

## What Does `.agg()` Do?

- **Summarizes your data** by applying a function (or several functions) to each column (default) or each row.
- You can pass in a single function, a list of functions, or even a dictionary to control which columns get which functions.

---

## Usage Patterns

You can use `.agg()` in a few ways:

- **Single function:**  
      `df.agg('sum')`  
      Applies `'sum'` to every column.

- **List of functions:**  
      `df.agg(['sum', 'min'])`  
      Returns both the sum and the minimum for each column.

- **Different functions per column:**  
      `df.agg({'A': ['sum', 'min'], 'B': ['min', 'max']})`  
      Computes different stats for different columns.

- **Custom names for results:**  
      `df.agg(x=('A', 'max'), y=('B', 'min'), z=('C', 'mean'))`  
      Lets you label each result row as you wish.

- **By row instead of column:**  
      `df.agg('mean', axis='columns')`  
      Calculates the mean for each row.

---

## Parameters

- **`func`**: Function, string, list, or dict.  
    What operations do you want to perform? Pass a function (`np.mean`), a string (`'sum'`), a list of them, or a dict mapping columns to functions.
- **`axis`**: 0 or 'index' (default) for columns, 1 or 'columns' for rows.
- **`*args`, `**kwargs`**: Extra arguments for your function(s).

---

## What It Returns

- **Scalar:** If you use `.agg()` on a Series (not a DataFrame) with a single function.
- **Series:** If you use a single function on a DataFrame.
- **DataFrame:** If you use multiple functions.

---

## Example

    import pandas as pd
    import numpy as np

    df = pd.DataFrame([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [np.nan, np.nan, np.nan]],
                      columns=['A', 'B', 'C'])

- **Aggregate by column, with multiple functions:**
      
      df.agg(['sum', 'min'])
      
    Output:
           A     B     C
    sum  12.0  15.0  18.0
    min   1.0   2.0   3.0

- **Different functions for different columns:**

      df.agg({'A': ['sum', 'min'], 'B': ['min', 'max']})
      
    Output:
           A    B
    sum  12.0  NaN
    min   1.0  2.0
    max   NaN  8.0

- **Aggregate over rows (axis=1):**

      df.agg('mean', axis='columns')
    Output:
    0    2.0
    1    5.0
    2    8.0
    3    NaN
    dtype: float64

---

## In Summary

- `.agg()` is a flexible way to summarize your DataFrame using one or many functions.
- Works column-wise (default) or row-wise (`axis='columns'`).
- Handles both built-in functions and custom ones.
- Lets you control exactly which stats you want, for which columns, and even how to label the results.

---

**Tip:**  
Use `.agg()` when you want **multiple summary statistics** in one go—faster and more flexible than calling each method separately!

---
