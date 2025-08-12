# Understanding Pandas `.cummax()` Method: A Natural Language Explainer

When you see `.cummax()` in Pandas, you’re looking at a method that returns the **cumulative maximum** over a Series or DataFrame—basically tracking the highest value seen so far at each point in the data.

## What Is `.cummax()` in Pandas?

- `.cummax()` is a method available on Pandas `Series` and `DataFrame` objects.
- It walks through your data in order and keeps the maximum value seen up to the current index.
- This is often useful for detecting peaks over time, running records, or performance milestones.

---

## What You Write and What Pandas Does

- **What you write:**  
    `df['column'].cummax()`

- **What Pandas does:**  
    Starts from the first row, looks at the value, and sets that as the current maximum.  
    For each subsequent row, it:
    - Compares the new value to the current maximum.
    - If the new value is higher, updates the maximum.
    - Otherwise, repeats the last maximum.

---

## Parameters

- `axis` (optional, default `0`):
    - `0` → process down rows (for each column).
    - `1` → process across columns (for each row).
- `skipna` (optional, default `True`):
    - Whether to ignore `NaN` values.
    - If `False`, `NaN` values will propagate.

---

## What It Returns

- If called on a Series: returns a Series of the same length with the cumulative max values.
- If called on a DataFrame: returns a DataFrame of the same shape with cumulative max calculated along the specified axis.

---

## Examples

**Series Example:**
    
    import pandas as pd
    s = pd.Series([3, 1, 4, 2, 5])
    s.cummax()
    # 0    3
    # 1    3
    # 2    4
    # 3    4
    # 4    5
    # dtype: int64

**DataFrame Example:**
    
    df = pd.DataFrame({
        'A': [2, 4, 3, 5],
        'B': [1, 2, 8, 0]
    })
    df.cummax()
    #    A  B
    # 0  2  1
    # 1  4  2
    # 2  4  8
    # 3  5  8

**Row-wise Cumulative Maximum:**
    
    df.cummax(axis=1)
    #    A  B
    # 0  2  2
    # 1  4  4
    # 2  3  8
    # 3  5  5

---

## Notes and Tips

- Use `.cummax()` when you want a “running maximum” rather than the overall max.
- It preserves the index and shape of the input.
- With time series data, this is often used to track record highs.

---

**Tip:**  
To learn more, run:
    
    help(pd.Series.cummax)
