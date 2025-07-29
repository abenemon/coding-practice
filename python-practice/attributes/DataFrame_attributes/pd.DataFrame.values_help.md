# Pandas `.values` Property — A Natural Language Explainer

The `.values` property in pandas returns the **raw data** of your DataFrame (or Series) as a **NumPy array**, stripping away all index and column labels. While it’s convenient, pandas now recommends using `.to_numpy()` instead for most purposes.

---

## What Is `.values`?

- `.values` is a property (no parentheses needed!).
- It returns the contents of your DataFrame as a NumPy array (`numpy.ndarray`).
- **Labels (index and columns) are removed**—only the data remains.

---

## Syntax

- For a DataFrame:  
  `df.values`
- For a Series:  
  `series.values`

---

## What Does It Return?

- A `numpy.ndarray` of the DataFrame’s data.
- The data type of the array will be the "lowest common denominator" needed to fit all column types (i.e., if you have mixed types, the array will have a broader type, often `object`).

---

## Why Use `.values`? When Should You Avoid It?

- Use `.values` when you want the raw data as a NumPy array (for use with NumPy/scikit-learn).
- **BUT:**  
  It’s now recommended to use `.to_numpy()` instead, which is more explicit and reliable, especially with new pandas features.

---

## Examples

- **Homogeneous DataFrame (all numeric):**
      
      import pandas as pd

      df = pd.DataFrame({
          'age': [3, 29],
          'height': [94, 170],
          'weight': [31, 115]
      })

      print(df)
      #    age  height  weight
      # 0    3      94      31
      # 1   29     170     115

      print(df.values)
      # array([[  3,  94,  31],
      #        [ 29, 170, 115]])

- **DataFrame with Mixed Types:**
      
      import numpy as np

      df2 = pd.DataFrame([
          ('parrot', 24.0, 'second'),
          ('lion', 80.5, 1),
          ('monkey', np.nan, None)
      ], columns=['name', 'max_speed', 'rank'])

      print(df2.values)
      # array([['parrot', 24.0, 'second'],
      #        ['lion', 80.5, 1],
      #        ['monkey', nan, None]], dtype=object)

---

## Important Notes

- **Dtype "Upcasting":**  
  If your DataFrame has mixed types, `.values` will upcast to the broadest type (often `object`).
  - Example: mix of `int32` and `uint8` becomes `int32`; mix of `int64` and `uint64` becomes `float64`.
- **No labels:**  
  The resulting NumPy array has no row or column labels—just the data.
- **For future code, use `.to_numpy()` instead of `.values`.**

---

## See Also

- `df.to_numpy()`: The recommended way to get a NumPy array from your DataFrame.
- `df.index`: Get index labels.
- `df.columns`: Get column names.

---

## Summary

- `.values` gives you the raw NumPy array of your data, with **no labels**.
- For most modern pandas code, **prefer `.to_numpy()`**.
- Be aware of dtype upcasting if your DataFrame contains mixed types.

---
