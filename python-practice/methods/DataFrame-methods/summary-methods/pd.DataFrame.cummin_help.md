# Understanding Pandas `.cummin()` Method: A Natural Language Explainer

When you see `.cummin()` in Pandas, you’re looking at a method that returns the **cumulative minimum** over a Series or DataFrame—tracking the smallest value seen so far at each point in the data.

## What Is `.cummin()` in Pandas?

- `.cummin()` is a method available on Pandas `Series` and `DataFrame` objects.
- It moves through your data in order and records the lowest value encountered up to the current index.
- This is often used for monitoring running lows, minimum records, or dips in performance.

---

## What You Write and What Pandas Does

- **What you write:**  
    `df['column'].cummin()`

- **What Pandas does:**  
    Starts from the first row, sets that value as the current minimum.  
    For each subsequent row:
    - If the new value is lower, updates the minimum.
    - If it’s higher, repeats the last minimum.

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

- Series input → Series of the same length with cumulative minimum values.
- DataFrame input → DataFrame of the same shape with cumulative minimum along the chosen axis.

---

## Examples

**Series Example:**
    
    import pandas as pd
    s = pd.Series([3, 1, 4, 2, 0])
    s.cummin()
    # 0    3
    # 1    1
    # 2    1
    # 3    1
    # 4    0
    # dtype: int64

**DataFrame Example:**
    
    df = pd.DataFrame({
        'A': [2, 4, 3, 1],
        'B': [5, 2, 8, 0]
    })
    df.cummin()
    #    A  B
    # 0  2  5
    # 1  2  2
    # 2  2  2
    # 3  1  0

**Row-wise Cumulative Minimum:**
    
    df.cummin(axis=1)
    #    A  B
    # 0  2  2
    # 1  4  2
    # 2  3  3
    # 3  1  0

---

## Notes and Tips

- `.cummin()` is the mirror image of `.cummax()`—it tracks running lows instead of highs.
- Keeps the same shape and index as the input.
- Works well with time series for detecting record lows.

---

**Tip:**  
To see full details, run:
    
    help(pd.Series.cummin)
