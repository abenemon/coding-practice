# Understanding `plt.title`: Setting Plot Titles in Matplotlib

When you run `help(plt.title)`, you’re looking at the function used to add a title to your Matplotlib plots. Here’s a beginner-friendly guide you can copy into a GitHub markdown file.

## What Does `plt.title` Do?
* `plt.title` sets the title above your plot (the “Axes”).
* You can control its text, position (left/center/right), style, and spacing.

## Basic Usage
* Typical usage: ``plt.title("Your Title")``
* This places the title above the plot, centered by default.

## Parameters Explained

- **label** (`str`):  
  The text you want as your plot title.  
  Example: ``plt.title("Sales Over Time")``

- **fontdict** (`dict`):  
  Dictionary to control the style of the title text (font size, weight, color, etc).  
  *Note: Using `fontdict` directly is discouraged—use keyword arguments instead or do ``plt.title(..., **fontdict)`` if needed.*
  Example:  
  ``plt.title("My Title", fontdict={'fontsize': 16, 'color': 'red'})``

- **loc** (`'left'`, `'center'`, `'right'`):  
  Choose where the title appears above the plot:  
  * ``plt.title("Left Title", loc='left')``  
  * ``plt.title("Center Title", loc='center')``  
  * ``plt.title("Right Title", loc='right')``

- **y** (`float`):  
  Controls how high the title is placed (1.0 is the very top of the Axes).  
  Example: ``plt.title("Higher Title", y=1.05)``

- **pad** (`float`):  
  Padding between the title and the plot (in points).  
  Example: ``plt.title("Tight Title", pad=5)``

- **kwargs**:  
  Any other text properties for fine-tuned control (e.g., `fontsize`, `color`, `weight`).  
  Example: ``plt.title("Styled", fontsize=18, color='purple', weight='bold')``

## Examples

``import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Default Centered Title")
plt.show()``

``plt.title("Left-aligned", loc='left', fontsize=14, color='green')``

``plt.title("Custom y & pad", y=1.10, pad=30, fontsize=16)``

``font_opts = {'fontsize': 20, 'fontweight': 'bold', 'color': 'navy'}
plt.title("Using fontdict", **font_opts)``

## Key Points

* **Returns**: a `Text` object (rarely needed for basic use).
* **Multiple titles**: By changing `loc`, you can set different titles at left, center, or right positions above the plot.
* **Custom style**: Prefer keyword arguments over `fontdict` for most styling.

## In Summary

* Use ``plt.title("Your Title")`` for basic plots.
* Use `loc`, `fontsize`, `color`, `pad`, and other kwargs for custom looks.
* Use ``plt.title(..., **fontdict)`` only if you have a dictionary of options.

Tip: For advanced options, check the [Matplotlib Text properties docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html).
