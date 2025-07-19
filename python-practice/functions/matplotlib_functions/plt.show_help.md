```
# Understanding `plt.show`: How to Display Plots in Matplotlib

When you look up `help(plt.show)` in Python, you’re seeing the command that **makes your plots appear in a window** (outside of Jupyter) or triggers the display of all your figures. Here’s how it works for beginners.

## What is `plt.show`?

* `plt.show()` is used to **display all open figures** created with Matplotlib.
* When you run it, any plot you’ve made with functions like `plt.plot()` appears in a window on your screen (in scripts, interactive shells, or most IDEs).

## Basic Usage

* Just call `plt.show()` after your plotting commands:
``import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()``
* All figures you’ve created since the last `plt.show()` will appear.

## The `block` Parameter

* `block` is an optional argument that controls how the plot window behaves:
  * `block=True`: **Waits** for you to close the plot window before your code continues (the default in non-interactive mode).
  * `block=False`: **Does not wait**—shows the window and your code keeps running. Use this if you want your script to keep going or are managing the GUI loop yourself.
* You can call it like: ``plt.show(block=False)``

## Interactive vs. Non-Interactive Mode

* In **interactive mode** (for example, if you call `plt.ion()`), plots update automatically and you usually don’t need to call `plt.show()`.
* In **non-interactive mode** (like most Python scripts), you must call `plt.show()` to see your plots.

## Using `plt.show` in Jupyter Notebooks

* In Jupyter, you **usually don’t need `plt.show()`** at all! The notebook displays your plots automatically at the end of a cell.
* If you do use it, it won’t cause problems—but it’s often not required.

## Saving vs. Showing

* If you want to **save a plot to a file** *and* show it on the screen, **save it before calling `plt.show()`**:
``plt.savefig("myplot.png")``
``plt.show()``
* After a blocking `plt.show()`, your figure is closed and can't be saved with `plt.savefig` unless you have a reference to the figure.

## Related Functions

* `plt.ion()` – Enable interactive mode (auto-updates the plot).
* `plt.ioff()` – Disable interactive mode.
* `plt.savefig()` – Save your figure as an image file (PNG, JPG, etc.).

## In summary

* Use `plt.show()` in scripts or interactive shells to display your plots.
* The `block` parameter controls whether your script waits for you to close the window.
* In Jupyter notebooks, you usually don’t need it.
* Save figures **before** you call `plt.show()` if you want to do both.

Tip: To see more details or special options, run `help(plt.show)` in your Python environment.
```
