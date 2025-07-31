# Using Custom Functions with `.agg()` in Pandas

Sometimes, built-in summary statistics (like `min`, `max`, `mean`) aren’t enough. The `.agg()` method lets you use **your own custom functions** to compute exactly what you want—such as the 30th percentile of a column.

---

## Step 1: Defining a Function in Python

A function is a reusable block of code. Here’s how you define one:

    def function_name(parameter):
        # code that does something
        return result

- **`def`** tells Python you’re defining a function.
- **`function_name`** is whatever you want to call your function.
- **`parameter`** is a placeholder for the input.
- **`return`** gives back the output.

---

## The Example: Calculating the 30th Percentile

In the video, the narrator writes:

      def pct30(column):
          return column.quantile(0.3)

What does this do?

- Defines a function called `pct30`.
- It takes in one argument, `column` (a pandas Series—like one column from your DataFrame).
- It returns the value at the 30th percentile (`quantile(0.3)`) of the column.

You don’t have to fully understand how `quantile` works yet—just know this function gives you the number where 30% of the dog weights are less than or equal to that value.

---

## Step 2: Using Your Function with `.agg()`

Now you can use this custom function just like any built-in function:

      dogs["weight_kg"].agg(pct30)

- This tells pandas:  
  “On the `weight_kg` column, run the `pct30` function and give me the result.”
- The output is the 30th percentile of dog weights.

---

## Step 3: Summaries on Multiple Columns

You can also get custom statistics for **more than one column at once**.  
Just select the columns you want before calling `.agg()`:

      dogs[["weight_kg", "height_cm"]].agg(pct30)

- This will calculate the 30th percentile for both the `weight_kg` and `height_cm` columns.
- The result is a summary for each column using your custom function.

---

## Step 4: Multiple Summaries at Once

What if you want **several custom statistics**?  
You can define more functions and pass a list of them into `.agg()`.

Example from the video:

      def pct40(column):
          return column.quantile(0.4)
      dogs["weight_kg"].agg([pct30, pct40])

- Here, `pct40` is a new function that calculates the 40th percentile.
- By passing `[pct30, pct40]`, pandas runs *both* functions on the `weight_kg` column.
- The result: you get both the 30th and 40th percentiles for the dogs’ weights, all at once.

---

## Why This Is Powerful

- You can write **any function** you want and use it in `.agg()`, letting you summarize your data in any way—not just with built-in statistics.
- `.agg()` works with a single column, many columns, or many functions—great for flexible, powerful data analysis!

---

## In Summary

- **Defining a function**: Write your own code to compute a custom statistic.
- **Using with `.agg()`**: Pass your function’s *name* (not a string!) to `.agg()`.
- **Multiple columns**: Select multiple columns and call `.agg()` for summaries on all of them.
- **Multiple summaries**: Pass a list of functions into `.agg()` to get several statistics at once.
- **Result**: Pandas runs your function(s) on your chosen column(s) and returns your custom summaries.

---

**Tip:**  
You don’t have to fully understand custom functions the first time you see them! For now, just remember: if you see `def ...`, someone is defining a little tool that can be used with `.agg()` for custom summaries.

---
