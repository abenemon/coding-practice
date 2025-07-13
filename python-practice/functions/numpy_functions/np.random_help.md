# Essentials of NumPy Random Number Generation (`np.random`)

The `np.random` module in NumPy is used for **generating random numbers**, random arrays, and performing random sampling.

---

## Key Concepts

- **Modern usage:**  
  Use the `numpy.random.Generator` class for new code.  
  The old global functions like `np.random.rand` and `np.random.randint` are still available but are considered legacy.

- **Creating a random generator:**  
    rng = np.random.default_rng(seed)
  - `seed` (optional): integer for reproducibility.

---

## Common Methods

- **Uniform random numbers (0 to 1):**
      rng.random(size)         # size can be int or tuple for shape

- **Random integers:**
      rng.integers(low, high, size)

- **Random choice from an array:**
      rng.choice(arr, size, replace=True)

- **Random permutation (shuffling):**
      rng.permutation(arr)

- **Random numbers from a normal (Gaussian) distribution:**
      rng.normal(loc=0.0, scale=1.0, size=None)

---

## Legacy Interface (still widely used)

- **Uniform random floats:**  
      np.random.rand(3, 2)       # Shape (3,2) array of floats in [0,1)

- **Random integers:**  
      np.random.randint(low, high=None, size=None)

- **Random choice:**  
      np.random.choice(arr, size=None)

- **Set global seed:**  
      np.random.seed(123)

---

## Example

    import numpy as np

    # New recommended way
    rng = np.random.default_rng(42)
    a = rng.random((2, 3))               # 2x3 array of floats in [0,1)
    b = rng.integers(1, 10, size=5)      # 5 random integers from 1 to 9
    c = rng.normal(0, 1, size=4)         # 4 random numbers from standard normal
    d = rng.choice([10, 20, 30], size=2) # Pick 2 random elements from array

    # Old way (works but less flexible)
    np.random.seed(42)
    e = np.random.rand(2, 3)
    f = np.random.randint(1, 10, size=5)

---

## Summary

- Use `np.random.default_rng()` to get a random generator (`rng`).
- Use methods like `rng.random()`, `rng.integers()`, `rng.choice()`, etc.
- For reproducibility, set the seed.
- Old functions still work but prefer the new generator for new projects.

---
