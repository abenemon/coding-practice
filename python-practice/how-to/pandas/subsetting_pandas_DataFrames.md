# Subsetting Pandas DataFrames: A Natural Language Explainer

Subsetting means zooming in on certain columns or rows of your DataFrame—the simplest way to find just the data you care about.

---

## Subsetting Columns

- To select a single column, use square brackets with the column name.

**Example:**
    `dogs["name"]`

- This returns just the `name` column as a Series.

---

## Subsetting Multiple Columns

- Use double square brackets with a list of column names.

**Example:**
    `dogs[["name", "height_cm"]]`

- This returns a new DataFrame with only the selected columns.

- You can also store your column names in a list variable and use it:

    ```
    cols_to_keep = ["name", "height_cm"]
    dogs[cols_to_keep]
    ```

---

## Subsetting Rows

- Most often done using a logical condition that evaluates to `True` or `False` for each row.

**Example:**
    `dogs["height_cm"] > 50`

- This gives you a Series of boolean values, `True` for rows where height is greater than 50.

---

- Use this condition inside square brackets to filter rows:

    `dogs[dogs["height_cm"] > 50]`

- This returns only the rows where height is greater than 50 cm.

---

## Subsetting Rows Based on Text Data

- Use the double equal sign `==` in your condition.

**Example:**
    `dogs[dogs["breed"] == "Labrador"]`

- This returns all Labradors.

---

## Subsetting Rows Based on Dates

- You can filter rows using date strings in the international format `YYYY-MM-DD`.

**Example:**
    `dogs[dogs["date_of_birth"] < "2015-01-01"]`

- This returns all dogs born before 2015.

---

## Subsetting Rows Based on Multiple Conditions

- Combine multiple logical conditions using `&` (and) or `|` (or).
- Wrap each condition in parentheses.

**Example:**
    `dogs[(dogs["height_cm"] > 60) & (dogs["color"] == "black")]`

- This filters for tall, black dogs.

---

## Subsetting Using `.isin()`

- Use `.isin()` to filter on multiple values in a column.

**Example:**
    `dogs[dogs["color"].isin(["black", "brown"])]`

- This returns all dogs whose color is black or brown.

---

## Summary

- Use single or double square brackets to subset columns.
- Use logical conditions inside square brackets to subset rows.
- Combine conditions with `&` and `|`.
- Use `.isin()` to match multiple values in a column.

---

**Tip:**  
Check out pandas’ documentation for more ways to filter and subset data!
