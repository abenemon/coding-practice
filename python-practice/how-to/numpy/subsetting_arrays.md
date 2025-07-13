# Subsetting NumPy Arrays: What’s Special, and What’s Familiar

NumPy arrays (`ndarray`) give you powerful ways to subset (select parts of) your data.  
While regular Python lists support basic indexing and slicing, NumPy arrays let you do much more, making it easy to work with multi-dimensional data and select complex patterns in a single step.

---

## Ways to Subset NumPy Arrays **Not Available** with Python Lists

### 1. **Boolean Indexing (Masking)**

- Select elements based on a condition, using a boolean array or condition.
- **Example:**
  - `a = np.array([10, 20, 30, 40])`
  - `mask = a > 20` → `array([False, False, True, True])`
  - `a[mask]` → `array([30, 40])`
  - Or all at once: `a[a % 20 == 0]` → `array([20, 40])`
- **Not possible with lists:**  
  - `[10, 20, 30, 40][[False, False, True, True]]` raises `TypeError`.

### 2. **Fancy Indexing (Indexing with Arrays or Lists of Indices)**

- Select multiple arbitrary elements or rows/columns at once using a list or array of indices.
- **Example:**
  - `a = np.array([10, 20, 30, 40])`
  - `a[[0, 2, 3]]` → `array([10, 30, 40])`
- **2D example:**
  - `b = np.array([[1, 2], [3, 4], [5, 6]])`
  - `b[[0, 2]]` → `array([[1, 2], [5, 6]])`
  - `b[[0, 2], [1, 0]]` → `array([2, 5])` (picks [0,1] and [2,0])

- **Not possible with lists:**  
  - `[10, 20, 30, 40][[0, 2, 3]]` raises `TypeError`.

### 3. **Multi-dimensional Indexing**

- Directly index into multiple dimensions using a comma-separated tuple.
- **Example:**
  - `a = np.array([[10, 20], [30, 40]])`
  - `a[1, 0]` → `30`
- **With lists:**  
  - `lst = [[10, 20], [30, 40]]`
  - `lst[1][0]` → `30` (must do one index at a time, not both together)

### 4. **Broadcasted Slicing & Advanced Slicing**

- NumPy supports advanced slicing and broadcasting patterns, including step sizes, negative strides, and using slices together with fancy indexing.

---

## Subsetting NumPy Arrays: Methods **Shared with Python Lists**

### 1. **Basic Indexing**

- **Single element:**
  - `a[2]` → third element
- **With lists:**  
  - `[10, 20, 30][2]` → `30`
  - `np.array([10, 20, 30])[2]` → `30`

### 2. **Slicing**

- **Syntax:** `start:stop:step`
  - `a[1:3]` → elements at positions 1 and 2
  - `a[::-1]` → reverses the array
- **With lists:**  
  - `[10, 20, 30, 40][1:3]` → `[20, 30]`
  - `np.array([10, 20, 30, 40])[1:3]` → `array([20, 30])`
- Both support negative steps and omitting start/stop/step.

---

## Summary Table

| Technique                        | Python List | NumPy Array |
|-----------------------------------|-------------|-------------|
| Single index (`a[2]`)             | ✅          | ✅          |
| Basic slice (`a[1:3]`)            | ✅          | ✅          |
| Reverse (`a[::-1]`)               | ✅          | ✅          |
| **Boolean mask (`a[a > 0]`)**     | ❌          | ✅          |
| **Fancy index (`a[[0, 2, 3]]`)**  | ❌          | ✅          |
| **Multi-dim index (`a[1, 0]`)**   | ❌          | ✅          |

---

## Why Does This Matter?

- **NumPy lets you select, modify, and analyze complex subsets of your data with a single expression,** without writing loops.
- This leads to cleaner, faster, and more expressive code—especially with large or multi-dimensional datasets.

---

## Quick Examples

```python
import numpy as np
a = np.arange(10)               # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Boolean indexing
a[a % 2 == 0]                   # array([0, 2, 4, 6, 8])

# Fancy indexing
a[[1, 3, 5, 7]]                 # array([1, 3, 5, 7])

# Multi-dimensional slicing
b = np.arange(12).reshape(3, 4) # array([[ 0,  1,  2,  3],
                                 #        [ 4,  5,  6,  7],
                                 #        [ 8,  9, 10, 11]])
b[1:, 2:]                       # array([[ 6,  7],
                                 #        [10, 11]])
b[[0, 2], [1, 3]]               # array([ 1, 11])
