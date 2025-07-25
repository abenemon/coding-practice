# Looping Over NumPy Arrays: 1D and 2D Iteration Explained

NumPy arrays are central to data science in Python. They work similarly to lists, but are more powerful for calculations and multi-dimensional data.

## Iterating Over a 1D NumPy Array

You can use a simple `for` loop to access each element in a 1D NumPy array, just like you would with a list.

    import numpy as np
    for x in np_height:
        print(str(x) + " inches")

- `np_height` is a 1D NumPy array containing heights.
- Each iteration gives you a single height value.

## Iterating Over a 2D NumPy Array

A 2D NumPy array is like a grid: it's made up of rows (1D arrays) stacked together.
If you use a basic `for` loop on a 2D array, you'll get each row (as a 1D array), not each individual number.

    for row in np_baseball:
        print(row)

- Each iteration gives you a 1D array (a row).

## How to Access Every Element in a 2D NumPy Array

To access each individual number in a 2D NumPy array, use `np.nditer()`:

    for var in np.nditer(np_baseball):
        print(var)

- This will print every element, one by one (first all heights, then all weights, etc.).
- `np.nditer()` works for arrays of any shape and gives you each scalar element in sequence.

## Summary Table

| Array Type   | Example Loop                              | What You Get Each Time      |
|--------------|-------------------------------------------|-----------------------------|
| 1D           | `for x in np_height:`                     | Each value (height)         |
| 2D (rows)    | `for row in np_baseball:`                 | Each row (1D array)         |
| 2D (values)  | `for var in np.nditer(np_baseball):`      | Each scalar value           |

## Key Points

- Use a basic `for` loop for 1D arrays.
- For 2D arrays, a basic `for` loop gives you each row.
- Use `np.nditer()` to iterate over every single value in a multi-dimensional array.
- This approach works for arrays with any number of dimensions.

## Practice Tip

Try printing out `type(x)` or `type(var)` inside your loops to see what you are getting with each iteration. This helps you understand the structure of your data.
