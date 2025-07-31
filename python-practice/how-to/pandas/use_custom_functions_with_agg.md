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

## Why This Is Powerful

- You can write **any function** you want and use it in `.agg()`, letting you summarize your data in any way—not just with built-in statistics.

---

## In Summary

- **Defining a function**: Write your own code to compute a custom statistic.
- **Using with `.agg()`**: Pass your function’s *name* (not a string!) to `.agg()`.
- **Result**: Pandas runs your function on the column and returns your custom summary.

---

**Tip:**  
You don’t have to fully understand custom functions the first time you see them! For now, just remember: if you see `def ...`, someone is defining a little tool that can be used with `.agg()`.

---
