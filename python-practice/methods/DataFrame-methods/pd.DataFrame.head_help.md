# Pandas `.head()` Method — Detailed Reference & Examples

The `.head()` method in pandas is used to return the first `n` rows of a DataFrame (or Series) **based on position**. It's handy for quickly checking if your object contains the data you expect.

---

## Basic Usage

- **Syntax:**  
  `df.head(n)`
- **Default:**  
  Returns the first 5 rows if `n` is not specified.

---

## Parameters

- `n` (int, default 5):  
  The number of rows to select from the top of the DataFrame.
  - If `n` is **positive**, returns the first `n` rows.
  - If `n` is **negative**, returns all rows **except** the last `|n|` rows (equivalent to `df[:n]`).

---

## Return Value

- Returns a new DataFrame (or Series) containing the selected rows.
- If `n` is larger than the number of rows, returns all rows.

---

## Examples

- **DataFrame Example:**
      
      import pandas as pd

      df = pd.DataFrame({
          'animal': [
              'alligator', 'bee', 'falcon', 'lion',
              'monkey', 'parrot', 'shark', 'whale', 'zebra'
          ]
      })

      # View the entire DataFrame
      print(df)

      # Viewing the first 5 lines (default)
      print(df.head())

      # Viewing the first 3 lines
      print(df.head(3))

      # For negative n: all rows except the last 3
      print(df.head(-3))

- **Sample outputs:**

      # df.head()
           animal
      0  alligator
      1        bee
      2     falcon
      3       lion
      4     monkey

      # df.head(3)
           animal
      0  alligator
      1        bee
      2     falcon

      # df.head(-3)
           animal
      0  alligator
      1        bee
      2     falcon
      3       lion
      4     monkey
      5     parrot

---

## Notes

- If `n` is negative, you get **all rows except the last |n|**.
- If `n` is greater than the number of rows, you simply get the whole DataFrame.
- The method works similarly for pandas Series.

---

## See Also

- `.tail(n)` — returns the last `n` rows.

---

**Tip:**  
Use `.head()` as your first step after loading or manipulating data to quickly inspect what you're working with!

---
