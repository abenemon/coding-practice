# Understanding Pandas `DataFrame.sort_index()`: A Natural Language Explainer

The `sort_index()` method in pandas sorts a DataFrame **by its labels** (row index or column names). It’s different from `sort_values()`, which sorts by the values inside the DataFrame.

---

## What Is `sort_index`?

- Sorts a DataFrame by **row index labels** (default) or **column labels** (`axis=1`).
- Can handle single-level and MultiIndex DataFrames.
- Returns a new DataFrame unless you set `inplace=True`.

---

## Basic Syntax

      DataFrame.sort_index(
          axis=0,
          level=None,
          ascending=True,
          inplace=False,
          kind="quicksort",
          na_position="last",
          sort_remaining=True,
          ignore_index=False,
          key=None
      )

- **axis**: `0` (rows, default) or `1` (columns).
- **level**: If using MultiIndex, choose which level(s) to sort by.
- **ascending**: `True` (default) for ascending, `False` for descending. Can pass a list for MultiIndex.
- **inplace**: If `True`, modifies the DataFrame in place.
- **kind**: Sorting algorithm (`"quicksort"`, `"mergesort"`, `"heapsort"`, `"stable"`).
- **na_position**: `'last'` (default) puts NaNs at the end, `'first'` puts them at the start.
- **sort_remaining**: For MultiIndex, whether to sort remaining levels after sorting the chosen one.
- **ignore_index**: If `True`, reset labels to `0, 1, …, n-1` after sorting.
- **key**: A function applied to the index values before sorting (vectorized, like `str.lower`).

---

## Examples

### 1. Sort rows by index (default)

      import pandas as pd
      df = pd.DataFrame([1, 2, 3, 4, 5],
                        index=[100, 29, 234, 1, 150],
                        columns=["A"])
      df

      # Output
            A
      100   1
      29    2
      234   3
      1     4
      150   5

      df.sort_index()

      # Output
           A
      1    4
      29   2
      100  1
      150  5
      234  3

---

### 2. Sort in descending order

      df.sort_index(ascending=False)

      # Output
           A
      234  3
      150  5
      100  1
      29   2
      1    4

---

### 3. Sort by column labels

      df2 = pd.DataFrame({
          "b": [1, 2],
          "a": [3, 4],
          "c": [5, 6]
      })
      df2

      # Output
         b  a  c
      0  1  3  5
      1  2  4  6

      df2.sort_index(axis=1)

      # Output
         a  b  c
      0  3  1  5
      1  4  2  6

---

### 4. Use a key function for custom sorting

      df3 = pd.DataFrame({"val": [1, 2, 3, 4]}, index=["A", "b", "C", "d"])
      df3

      # Output
         val
      A    1
      b    2
      C    3
      d    4

      df3.sort_index(key=lambda x: x.str.lower())

      # Output
         val
      A    1
      b    2
      C    3
      d    4

Here, the sort is case-insensitive.

---

## In summary

- `sort_index()` orders a DataFrame by its **labels** (row or column).
- Use `axis=0` for rows (default) and `axis=1` for columns.
- Customize with `ascending`, `key`, and `level` (for MultiIndex).
- Returns a new DataFrame unless `inplace=True`.

---

**Tip:**  
Use `sort_values()` when you want to sort by **data values** inside the DataFrame, and `sort_index()` when you want to sort by **labels**.
