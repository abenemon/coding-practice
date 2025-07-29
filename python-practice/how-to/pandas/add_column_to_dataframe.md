# Two Ways to Add a Column to a Pandas DataFrame: For Loop vs. Apply

When you want to add a new column to a pandas `DataFrame` based on existing data, there are a few approaches. Here are two common methods—using a `for` loop with `iterrows()`, and using the faster, more "pandas-friendly" `apply()` function.

---

## 1. Using a For Loop and `iterrows()`

This method loops over each row in the DataFrame and assigns a new value by setting it directly using `.loc`.  
It's a very "explicit" and readable approach, but can be **slow** on large DataFrames.

**Example: Add a column with the length of each country name**

    import pandas as pd
    brics = pd.read_csv("brics.csv", index_col = 0)
    for lab, row in brics.iterrows():
          # Creating Series on every iteration
          brics.loc[lab, "name_length"] = len(row["country"])
    print(brics)

- `iterrows()` returns each row as a `(label, Series)` pair.
- On each loop, you calculate the new value and assign it using `.loc`.
- **Why it's inefficient:** Pandas must "re-build" parts of the DataFrame on every assignment, making this slow for big data.

---

## 2. Using `apply()` (the Efficient Way)

`apply()` lets you run a function on every value in a Series, returning a new Series. This is **vectorized** and much faster—it's the "pandas way."

**Example: Add the same column, but with `apply()`**

    import pandas as pd
    brics = pd.read_csv("brics.csv", index_col = 0)
    brics["name_length"] = brics["country"].apply(len)
    print(brics)

- `brics["country"]` gives you the Series of country names.
- `.apply(len)` applies the `len()` function to every value.
- The result is a new Series with the lengths, added directly as a column.

---

## Comparison

- **For loop with `iterrows()`**
    - Easy to understand, works for any custom logic.
    - Slow for large DataFrames (row-by-row assignment is not efficient in pandas).
- **`apply()`**
    - Much faster (especially for big data).
    - Code is shorter and clearer.
    - Only works if your calculation can be done row-wise or on a single column.

---

## TL;DR

- Use a for loop with `iterrows()` for simple scripts or when learning, but switch to `apply()` (or other vectorized methods) for real projects or large datasets.

---

**Pro tip:**  
Most tasks that require adding a column based on other columns can be done without explicit loops—using pandas vectorized operations, `.apply()`, or built-in methods (like `str.len()` for string length).

