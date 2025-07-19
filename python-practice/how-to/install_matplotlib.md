# How to Install and Import `matplotlib` in Python (2025 Guide)

If you want to use `matplotlib`—the go-to library for making charts and graphs in Python—you’ll first need to **install** it (if it’s not already installed), and then **import** it into your script or notebook.

---

## 1. How to Install `matplotlib`

- The easiest way is to use **pip**, Python’s package installer.
- Open your **Command Prompt** (Windows), **Terminal** (Mac/Linux), or your code editor’s built-in terminal.

**Run this command:**

``pip install matplotlib``

- This downloads and installs the latest version of `matplotlib` from the Python Package Index (PyPI).
- If you are using a **Jupyter Notebook**, you can run the same command from a notebook cell by putting an exclamation mark before it:

``!pip install matplotlib``

**If you are using Anaconda or Miniconda:**

- You can also install using conda:

``conda install matplotlib``

---

## 2. How to Import `matplotlib` in Your Code

After installation, you can import it into your Python script or notebook.  
Most people use the `pyplot` module (which is part of `matplotlib`) and import it with an alias for convenience.

**Typical import:**

``import matplotlib.pyplot as plt``

This lets you use all the main plotting functions using the shorter name ``plt`` (for example: ``plt.plot()``, ``plt.show()``).

---

## 3. Quick Example

Here’s how you might make sure it’s working:

``import matplotlib.pyplot as plt``
``plt.plot([1, 2, 3], [4, 5, 6])``
``plt.show()``

If you see a simple line plot appear, you’re good to go!

---

## Troubleshooting

- **If you see "ModuleNotFoundError: No module named 'matplotlib'":**
    - Double-check that you installed `matplotlib` in the same Python environment you’re running your script or notebook in.
    - Try running ``pip show matplotlib`` to see where it’s installed.

- **If using multiple Python versions:**
    - You might need to use ``pip3`` instead of ``pip``, like this: ``pip3 install matplotlib``

---

## In summary

- **Install** using ``pip install matplotlib`` (or ``conda install matplotlib`` if using Anaconda).
- **Import** with ``import matplotlib.pyplot as plt``.
- Start making plots!

---

**Tip:**  
If you run into issues, check your Python environment and ensure you’re using the correct version of pip or conda for your setup.

---
