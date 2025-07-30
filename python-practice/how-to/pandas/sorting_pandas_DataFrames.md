# Sorting Pandas DataFrames: A Natural Language Explainer

Sorting is one of the simplest and most important ways to bring interesting data to the top of your DataFrame. In pandas, sorting is most often done with the `sort_values` method.

---

## How to Sort Rows in a DataFrame

- Use the `.sort_values()` method on your DataFrame.
- Pass in the column name you want to sort by.

**Example:**
    `dogs.sort_values("weight_kg")`

- This puts the lightest dog at the top, and the heaviest at the bottom.

---

## Sorting in Descending Order

- By default, `.sort_values()` sorts from smallest to largest.
- To sort the other way (largest to smallest), set the `ascending` argument to `False`.

**Example:**
    `dogs.sort_values("weight_kg", ascending=False)`

- Now, the heaviest dog is at the top and the lightest at the bottom.

---

## Sorting by Multiple Columns

- You can sort by more than one variable by passing a list of column names.

**Example:**
    `dogs.sort_values(["weight_kg", "height_cm"])`

- This sorts first by weight, then by height for rows with the same weight.

---

## Sorting by Multiple Columns in Different Orders

- To specify a different sort order for each column, pass a list to the `ascending` argument.

**Example:**
    `dogs.sort_values(["weight_kg", "height_cm"], ascending=[True, False])`

- In this example, pandas will sort by weight in ascending order, and by height in descending order for tied weights.

---

## Summary

- Use `.sort_values()` to reorder rows based on column values.
- Control direction with `ascending`.
- Sort by multiple columns with a list.
- Use a list with `ascending` to set different directions for each column.

---

**Tip:**  
Check the pandas documentation for more details:  
`help(pd.DataFrame.sort_values)`
