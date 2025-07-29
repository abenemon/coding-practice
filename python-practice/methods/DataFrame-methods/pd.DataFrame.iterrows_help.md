# Understanding the `iterrows()` Method in pandas DataFrames

When working with pandas DataFrames, you sometimes need to loop through each row to access its data one row at a time. The `iterrows()` method makes this possible by letting you iterate over rows as (index, row) pairs.

## What Is `iterrows()`?

- `iterrows()` is a pandas DataFrame method.
- It returns an iterator that produces two values at each step:
    - The **index** of the row.
    - The **row** itself, represented as a pandas Series.

## Basic Usage

    import pandas as pd
    for index, row in df.iterrows():
        print(index)
        print(row)

- `df` is your DataFrame.
- On each iteration:
    - `index` gives you the row label (often just the row number, unless you’ve set a custom index).
    - `row` is a Series containing all the data in that row, accessible by column names.

## Example

Suppose you have this DataFrame:

    data = {
        'name': ['Alice', 'Bob'],
        'age': [25, 30]
    }
    df = pd.DataFrame(data)

Looping with `iterrows()`:

    for idx, row in df.iterrows():
        print("Index:", idx)
        print("Name:", row['name'], "| Age:", row['age'])

**Output:**

    Index: 0
    Name: Alice | Age: 25
    Index: 1
    Name: Bob | Age: 30

## Key Points and Limitations

- Each `row` is a pandas Series, not a dictionary.
- If you modify `row` inside the loop, it does NOT change the original DataFrame.
- `iterrows()` is convenient for small DataFrames, but it is **slow for large datasets**—vectorized operations are much faster and preferred when possible.
- The data type of each row’s values may be upcast (e.g., int to float) to accommodate mixed types.

## When to Use

- When you need to examine or process rows one at a time.
- When you need both the row’s index and its data together.
- Not recommended for performance-critical code on large DataFrames.

## Summary

- `iterrows()` lets you loop through rows of a DataFrame as (index, Series) pairs.
- Ideal for quick inspection or row-wise operations on small DataFrames.
- For large data or performance-sensitive code, use vectorized pandas methods instead.
