# Understanding Pandas’ `DataFrame.median()` Method: A Natural Language Explainer

When you see `df.median()` in pandas, you’re using a built-in method to find the **median** (middle value) of each numeric column or row in your DataFrame.

---

## What Does `DataFrame.median()` Do?

- Calculates the median (the middle value when numbers are sorted) for each column (by default) or row in a DataFrame.
- Ignores non-numeric columns automatically.
- Returns a Series containing the median values.

---

## Syntax

    df.median(axis=0, skipna=True, numeric_only=False, **kwargs)

---

## Parameters

- `axis`:
    - `0` or `'index'` (default): Compute the median for each column (vertical, top-to-bottom).
    - `1` or `'columns'`: Compute the median for each row (horizontal, left-to-right).

- `skipna`:
    - `True` (default): Ignore `NaN` (missing) values when calculating the median.
    - `False`: If there’s any missing value in the row/column, the result will be `NaN`.

- `numeric_only`:
    - `None`/`False` (default): Try to include all numeric columns, may error on non-numeric data if `axis=1`.
    - `True`: Only include numeric columns.

---

## What Does It Return?

- A pandas `Series` with the median value for each column (or row, if `axis=1`).
- If used on a single column (like `df['col'].median()`), it returns a single number—the median for that column.

---

## Examples

- **Basic usage:**

      import pandas as pd
      df = pd.DataFrame({
          'A': [1, 2, 100],
          'B': [4, 5, 6],
          'C': ['x', 'y', 'z']
      })
      df.median()
      # Output:
      # A    2.0
      # B    5.0
      # dtype: float64

- **Median across rows (`axis=1`):**

      df.median(axis=1)
      # Output:
      # 0    2.5
      # 1    3.5
      # 2   53.0
      # dtype: float64

- **With missing values (`skipna=True` vs. `skipna=False`):**

      df2 = pd.DataFrame({'A': [1, None, 3], 'B': [4, 5, None]})
      df2.median()
      # Output:
      # A    2.0
      # B    4.5
      # dtype: float64

      df2.median(skipna=False)
      # Output:
      # A   NaN
      # B   NaN
      # dtype: float64

---

## Tips and Notes

- The median is less sensitive to outliers than the mean, so it can be useful for skewed data.
- Only works on columns (or rows) with numeric data—other types are ignored.
- Like most pandas methods, handles missing data by default.

---

**In summary:**
- `DataFrame.median()` finds the “middle value” for each numeric column or row.
- Skips missing data unless you tell it not to.
- Great for understanding the typical value in each part of your data.

---
