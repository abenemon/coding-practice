# Understanding `plt.scatter`: Making Scatter Plots in Matplotlib

If you want to make a scatter plot—dots (not lines) showing the relationship between two sets of numbers—use `plt.scatter` from Matplotlib’s `pyplot` module. Here’s a beginner’s guide based on `help(plt.scatter)`:

## What Is `plt.scatter`?

* `plt.scatter(x, y)` draws a **scatter plot**: each point has an x and y coordinate, and appears as a marker on the graph.
* Scatter plots are great for visualizing the relationship between two variables or showing distributions and clusters.

## Basic Usage

* Minimal call: ``plt.scatter(x, y)``
  * `x` and `y` should be sequences of the same length (like lists or arrays).
* By default, all points are the same size and color.

## Key Parameters

* `x`, `y` – The positions of the data points. Each must be a list, array, or similar.
* `s` – Size of the markers (in points squared). Can be a single number or a sequence (one size per point).
* `c` – Colors of the markers. Can be a single color, a sequence of colors, or numbers mapped to a colormap (for color gradients).
* `marker` – Shape of the marker (like `'o'` for circles, `'^'` for triangles, etc.).
* `cmap` – If you use numbers for `c`, `cmap` sets the color map (for gradients).
* `norm`, `vmin`, `vmax` – Control how numerical values are mapped to colors (for advanced use).
* `alpha` – Transparency, from 0 (transparent) to 1 (opaque).
* `linewidths` – Line width of the marker edges.
* `edgecolors` – Color of the marker edges.
* `data` – Allows use with pandas DataFrames or dicts: `plt.scatter('colA', 'colB', data=df)`.
* `plotnonfinite` – Whether to plot non-finite (NaN or inf) values.

## Returns

* `plt.scatter` returns a **PathCollection object**, which represents all the dots drawn.

## Example Usage

``import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 14]
sizes = [20, 50, 80, 200, 500]    # Marker sizes
colors = [100, 200, 300, 400, 500] # Color by value

plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.7)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("A Simple Scatter Plot")
plt.colorbar(label="Color scale")
plt.show()``

## Tips

* If you just want a simple scatterplot with identical markers, you can use `plt.plot(x, y, 'o')`—but `plt.scatter` lets you control each marker’s size and color individually.
* Use the `cmap` parameter to apply a colormap when `c` is an array of numbers.
* To hide marker edges, set `edgecolors='none'` or `linewidth=0`.

## When to Use `plt.scatter` vs. `plt.plot`
* Use `plt.scatter` when you want to vary marker size and/or color for each point.
* Use `plt.plot(..., 'o')` for very simple scatterplots with identical markers.

## In summary

* `plt.scatter` is the go-to for customizable scatter plots.
* It lets you change marker size, color, shape, and more.
* Great for exploring relationships, clusters, and distributions in data.

Tip: For all the details and style options, check the [Matplotlib documentation for scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html) or run `help(plt.scatter)`.
