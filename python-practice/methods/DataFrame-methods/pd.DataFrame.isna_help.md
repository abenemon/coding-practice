# Understanding Pandas `DataFrame.isna()`: A Natural Language Explainer

When working with data in Pandas, you’ll often need to check for **missing values** (like `NaN` or `None`). The `DataFrame.isna()` method is a quick way to create a “mask” showing where the missing values are.

---

## What Is `DataFrame.isna()`?

- `isna()` is a method in Pandas used to detect missing values in a DataFrame.
- It returns another DataFrame of the same shape, filled with **boolean values**:
  - `True` where a value is missing (`NaN` or `None`).
  - `False` where a value is present.

---

## What You Write and What Pandas Does

- **What you write:**  
    `df.isna()`

- **What Pandas does:**  
    It looks at every element in the DataFrame and checks whether it’s missing.  
    The result is a new DataFrame of booleans.

---

## Parameters

`DataFrame.isna()` takes **no parameters**. It just runs on the DataFrame it’s called on.

---

## What It Returns

- A new `DataFrame` of the same size.
- Each entry is `True` if the original value was missing, otherwise `False`.

---

## Examples

- **Simple DataFrame example:**

      import pandas as pd
      import numpy as np

      df = pd.DataFrame({
          "A": [1, 2, np.nan],
          "B": ["x", None, "z"]
      })
      print(df)

      # Output:
      #      A     B
      # 0  1.0     x
      # 1  2.0  None
      # 2  NaN     z

      df.isna()

      # Output:
      #        A      B
      # 0  False  False
      # 1  False   True
      # 2   True  False

---

## Common Use Cases

- **Count missing values per column:**

      df.isna().sum()

- **Find rows with missing values:**

      df[df.isna().any(axis=1)]

- **Check if any missing values exist in the whole DataFrame:**

      df.isna().values.any()

---

## Related Methods

- `DataFrame.notna()` → Opposite of `isna()`, marks non-missing values as `True`.
- `Series.isna()` → Works the same way but for a single column or Series.
- `DataFrame.fillna()` → Replace missing values with something else.
- `DataFrame.dropna()` → Remove missing values.

---

## In summary

- `df.isna()` highlights missing values in your DataFrame with a boolean mask.  
- Use it with `.sum()`, `.any()`, or `.all()` to quickly analyze missing data.  
- Combine with `fillna()` or `dropna()` to handle those missing values.

---
