# Pandas `.sort_values()` Method — A Natural Language Explainer

The `.sort_values()` method lets you **sort the rows of your DataFrame** by the values in one or more columns. It’s one of the most important tools for ordering your data, finding top values, or preparing for analysis and plotting.

---

## What Does `.sort_values()` Do?

- Rearranges the rows of your DataFrame based on the values in specified column(s).
- Can sort by one column, multiple columns, in ascending or descending order.
- You choose whether to sort in-place (modifying the original DataFrame) or return a sorted copy.

---

## Syntax

    df.sort_values(
        by,
        axis=0,
        ascending=True,
        inplace=False,
        kind='quicksort',
        na_position='last',
        ignore_index=False,
        key=None
    )

- `df` is your DataFrame variable.

---

## Key Parameters

- `by` (str or list of str):  
  The column(s) (or row/column labels, with `axis`) to sort by.

- `axis` (0 or 1):  
  `0` (default): sort rows by column values.  
  `1`: sort columns by row values.

- `ascending` (bool or list of bool, default `True`):  
  Sort ascending (`True`) or descending (`False`). List for multi-column sorting.

- `inplace` (bool, default `False`):  
  If `True`, sorts the DataFrame in-place (no return). If `False`, returns a new sorted DataFrame.

- `na_position` (`'first'` or `'last'`, default `'last'`):  
  Where to put `NaN` values—at the top or bottom.

- `ignore_index` (bool, default `False`):  
  If `True`, the index will be reset (0, 1, ...).

- `key` (callable, optional):  
  Function to apply to values before sorting (for custom or "natural" sorts).

---

## What Does It Return?

- By default, returns a **new sorted DataFrame** (unless `inplace=True`, in which case returns `None`).

---

## Examples

- **Basic sorting by a column:**
      
      import pandas as pd
      import numpy as np

      df = pd.DataFrame({
          'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
          'col2': [2, 1, 9, 8, 7, 4],
          'col3': [0, 1, 9, 4, 2, 3],
          'col4': ['a', 'B', 'c', 'D', 'e', 'F']
      })

      # Sort by 'col1' (ascending)
      sorted_df = df.sort_values(by='col1')
      print(sorted_df)

- **Sort by multiple columns:**
      
      sorted_df = df.sort_values(by=['col1', 'col2'])

- **Descending order:**
      
      sorted_df = df.sort_values(by='col1', ascending=False)

- **Place NaNs first:**
      
      sorted_df = df.sort_values(by='col1', na_position='first')

- **Reset index after sorting:**
      
      sorted_df = df.sort_values(by='col1', ignore_index=True)

- **Sort using a key (e.g., case-insensitive):**
      
      sorted_df = df.sort_values(by='col4', key=lambda col: col.str.lower())

---

## See Also

- `df.sort_index()`: Sort DataFrame by row or column index.
- `series.sort_values()`: Sort a pandas Series.

---

## Summary

- `.sort_values()` is the main way to reorder DataFrame rows by column values.
- Supports sorting by one or more columns, with many options for order, handling NaNs, and index resetting.
- For custom sorts, use the `key` parameter with a function.

---
