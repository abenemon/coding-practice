# Understanding Pandas `.cumsum()`: A Natural Language Explainer

When you see `.cumsum()` in pandas, think: **"Cumulative Sum"**. This method lets you create a new Series or DataFrame where each value is the running total of the values that came before it.

---

## What Is `.cumsum()` in Pandas?

- `.cumsum()` stands for **cumulative sum**.
- It calculates the sum of a sequence of numbers, element by element, up to the current point.
- Works with both pandas Series (a single column) and DataFrame (multiple columns).

---

## What You Write and What Pandas Does

- **What you write:**
    - For a Series:  
        `series.cumsum()`
    - For a DataFrame:  
        `df.cumsum()`

- **What pandas does:**  
    - For each element, adds up all previous elements (including the current one).
    - Returns a new Series or DataFrame with these running totals.

---

## Parameters

- **`axis`** (default `0`):  
    - Determines the direction of the cumulative sum.
    - `0` or `'index'`: sum **down** each column (the default).
    - `1` or `'columns'`: sum **across** each row.

- **`skipna`** (default `True`):  
    - Whether to skip `NaN` (missing) values.
    - If `True`, missing values are ignored; the sum picks up after the missing data.
    - If `False`, cumulative sum becomes `NaN` after the first missing value.

---

## What It Returns

- A new Series or DataFrame of the same shape as the original, where each value is the cumulative sum up to that point.

---

## Examples

- **Basic Series Example:**

      import pandas as pd
      s = pd.Series([1, 2, 3, 4])
      s.cumsum()
      # 0    1
      # 1    3
      # 2    6
      # 3   10
      # dtype: int64

- **DataFrame Example:**

      df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
      df.cumsum()
      #    a   b
      # 0  1   4
      # 1  3   9
      # 2  6  15

- **Handling Missing Values:**

      s = pd.Series([1, None, 2, 3])
      s.cumsum()
      # 0    1.0
      # 1    1.0
      # 2    3.0
      # 3    6.0
      # dtype: float64

      s.cumsum(skipna=False)
      # 0    1.0
      # 1    NaN
      # 2    NaN
      # 3    NaN
      # dtype: float64

- **Row-wise Cumulative Sum:**

      df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
      df.cumsum(axis=1)
      #    a  b
      # 0  1  5
      # 1  2  7
      # 2  3  9

---

## When Would You Use `.cumsum()`?

- Tracking running totals (e.g., sales over time, cumulative rainfall, account balances).
- Data transformations for time series or financial analysis.
- Building features for machine learning where cumulative context matters.

---

## In summary

- `.cumsum()` gives you the running total along a pandas Series or DataFrame.
- It’s easy to use, works with missing data (if you want), and is perfect for adding up data as you go.
- Use the `axis` and `skipna` parameters to control direction and handling of missing values.

---

**Tip:**  
To see more, try:

    help(pd.Series.cumsum)
    help(pd.DataFrame.cumsum)

---
