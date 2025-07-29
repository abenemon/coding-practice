# Pandas `.shape` Property — A Natural Language Explainer

The `.shape` property is the quickest way to find out the **dimensions** (number of rows and columns) of your pandas DataFrame or Series. It's an essential tool for checking your data’s structure at a glance.

---

## What Is `.shape` in pandas?

- `.shape` is a property (not a method—no parentheses needed!).
- It returns a **tuple** representing the dimensions of your DataFrame:
    - The first value is the number of **rows**.
    - The second value is the number of **columns**.

---

## Syntax

- For a DataFrame:  
  `df.shape`
- For a Series:  
  `series.shape`

  - `df` or `series` is your DataFrame or Series variable.

---

## What Does It Return?

- A tuple: `(number_of_rows, number_of_columns)`
    - For Series, just `(number_of_items,)`

---

## Why Use `.shape`?

- **Quickly check** how much data you have.
- Useful for debugging, reshaping, or when reading data from files.
- Helps you write code that depends on the size of your data.

---

## Examples

- **Basic Example (DataFrame):**
      
      import pandas as pd

      df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
      print(df.shape)
      # Output: (2, 2)
      # (2 rows, 2 columns)

      df2 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4], 'col3': [5, 6]})
      print(df2.shape)
      # Output: (2, 3)
      # (2 rows, 3 columns)

- **Series Example:**
      
      s = pd.Series([10, 20, 30])
      print(s.shape)
      # Output: (3,)

---

## See Also

- `ndarray.shape` — works the same way for NumPy arrays.

---

## Summary

- Use `.shape` to instantly know how many rows and columns are in your DataFrame.
- No parentheses—just write `df.shape`.
- Great for sanity-checking data at every step of your workflow!

---
