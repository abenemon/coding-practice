# How to Subset Lists of Lists in Python: A Quick Guide

A **list of lists** (sometimes called a “2D list” or “nested list”) is just a list where each item is itself a list.  
For example:

    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

You often want to **subset** (select parts of) these structures:  
- Get a row or a column  
- Get a single value  
- Get a sub-grid  
- Get multiple rows/columns

---

## Accessing Elements in a List of Lists

### 1. Get a Single Item

- **What you write:**  
    `grid[row][col]`
- **What it does:**  
    Selects the item at position (`row`, `col`).

    Example:  
    `grid[1][2]`    # 6 (row index 1, column index 2)

---

### 2. Get a Whole Row

- **What you write:**  
    `grid[row]`
- **What it does:**  
    Gets the list at index `row`.

    Example:  
    `grid[0]`       # [1, 2, 3]

---

### 3. Get a Whole Column

- **What you write:**  
    `[row[col] for row in grid]`
- **What it does:**  
    Loops through each row, picking the item at column `col`.

    Example:  
    `[row[1] for row in grid]`   # [2, 5, 8] (all items in column 1)

---

### 4. Get a Sub-grid (Slice)

- **Rows 1 to 2, columns 0 to 1:**  
    `[row[0:2] for row in grid[1:3]]`   # [[4, 5], [7, 8]]

---

### 5. Get Multiple Rows

- **What you write:**  
    `grid[start:stop]`
- **What it does:**  
    Returns a list of rows from `start` up to (but not including) `stop`.

    Example:  
    `grid[0:2]`      # [[1, 2, 3], [4, 5, 6]]

---

### 6. Get Multiple Columns (as sublists)

- **What you write:**  
    `[row[start_col:stop_col] for row in grid]`
- **What it does:**  
    For each row, gets columns from `start_col` up to `stop_col`.

    Example:  
    `[row[1:3] for row in grid]`    # [[2, 3], [5, 6], [8, 9]]

---

## Summary Table

| Task                     | Example Code                     | Result                |
|--------------------------|----------------------------------|-----------------------|
| Single item (2nd row, 3rd col) | `grid[1][2]`                 | 6                     |
| Whole row (first row)    | `grid[0]`                        | [1, 2, 3]             |
| Whole column (second col)| `[row[1] for row in grid]`        | [2, 5, 8]             |
| Sub-grid (rows 1-2, cols 0-1) | `[row[0:2] for row in grid[1:3]]` | [[4, 5], [7, 8]]      |
| Multiple rows            | `grid[0:2]`                      | [[1, 2, 3], [4, 5, 6]]|
| Multiple columns         | `[row[1:3] for row in grid]`      | [[2, 3], [5, 6], [8, 9]] |

---

## Tips

- Indexing starts at 0 in Python.
- Negative indices count from the end: `grid[-1]` is the last row.
- Use slices (`start:stop`) to get ranges.
- List comprehensions let you pull out columns or blocks easily.

---

**Try it out:**  
Change the indices or slices above to experiment with your own data!

---
