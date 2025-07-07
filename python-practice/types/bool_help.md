# Understanding Python’s `bool` Class: A Natural Language Explainer

When you see `class bool(int)` in Python’s help system, you’re looking at Python’s **boolean** type—a type for representing truth values: `True` and `False`.

---

## What Is `bool` in Python?

- `bool` is the built-in type for logical truth values in Python.
- There are only two instances: `True` and `False`.
- `bool` is actually a subclass of `int`, so `True` acts like `1`, and `False` acts like `0` in arithmetic.
- You cannot create subclasses of `bool`.

Examples:

```python
flag = True
is_valid = False
print(type(flag))     # <class 'bool'>
print(True + True)    # 2 (since True is 1)
print(False * 10)     # 0 (since False is 0)
```

---

## Creating Booleans

- **Default (no argument):**
    ```python
    x = bool()      # False
    ```
- **From a value:**  
    `bool(x)` returns `False` if `x` is "falsy" (like 0, empty string, empty list, etc.), otherwise `True`.

    ```python
    bool(0)         # False
    bool(1)         # True
    bool("")        # False
    bool("hello")   # True
    bool([])        # False
    ```

---

## Special Methods and What They Mean

These are the “dunder” methods (`__something__`) that allow booleans to interact with operators and built-in functions.

---

## __and__(self, value)

- **What you write:**
    ```
    x & y
    ```
- **What Python does:**
    ```
    x.__and__(y)
    ```
- **What it means:**
    Bitwise AND operation. With booleans, this is like logical "and" (True only if both are True).

- **Example:**
    ```python
    True & False   # False
    True & True    # True
    ```

---

## __or__(self, value)

- **What you write:**
    ```
    x | y
    ```
- **What Python does:**
    ```
    x.__or__(y)
    ```
- **What it means:**
    Bitwise OR operation. With booleans, this is like logical "or" (True if at least one is True).

- **Example:**
    ```python
    True | False   # True
    False | False  # False
    ```

---

## __xor__(self, value)

- **What you write:**
    ```
    x ^ y
    ```
- **What Python does:**
    ```
    x.__xor__(y)
    ```
- **What it means:**
    Bitwise XOR (exclusive or): True if exactly one of the values is True.

- **Example:**
    ```python
    True ^ False   # True
    True ^ True    # False
    ```

---

## __invert__(self)

- **What you write:**
    ```
    ~x
    ```
- **What Python does:**
    ```
    x.__invert__()
    ```
- **What it means:**
    Bitwise NOT: flips all the bits. For booleans, `~True` is `-2`, `~False` is `-1` (because of how bools inherit from int). Not typically used on booleans.

- **Example:**
    ```python
    ~True      # -2
    ~False     # -1
    ```

---

## __repr__(self)

- **What you write:**
    ```
    repr(x)
    ```
- **What Python does:**
    ```
    x.__repr__()
    ```
- **What it means:**
    Returns the string `'True'` or `'False'`.

- **Example:**
    ```python
    repr(True)    # 'True'
    ```

---

## __rand__(self, value)

- **What you write:**
    ```
    y & x
    ```
- **What Python does:**
    ```
    x.__rand__(y)
    ```
- **What it means:**
    Handles bitwise AND when bool is on the right-hand side.

---

## __ror__(self, value)

- **What you write:**
    ```
    y | x
    ```
- **What Python does:**
    ```
    x.__ror__(y)
    ```
- **What it means:**
    Handles bitwise OR when bool is on the right-hand side.

---

## __rxor__(self, value)

- **What you write:**
    ```
    y ^ x
    ```
- **What Python does:**
    ```
    x.__rxor__(y)
    ```
- **What it means:**
    Handles bitwise XOR when bool is on the right-hand side.

---

## __new__(*args, **kwargs) (static method)

- **What it means:**
    Actually creates the boolean object. Normally, you don’t need to use this directly.

---

## Methods Inherited from int

Because `bool` is a subclass of `int`, it inherits many methods from `int` (such as `__add__`, `__eq__`, `__int__`, `__abs__`, etc.), so you can use booleans almost anywhere integers are expected.

Examples:

```python
int(True)      # 1
int(False)     # 0
abs(True)      # 1
True + 5       # 6
```

See the [int explainer](./int.md) for detailed explanations of those methods.

---

## Data Descriptors

- **denominator**: Always 1.
- **imag**: Always 0 (for complex compatibility).
- **numerator**: 1 for True, 0 for False.
- **real**: 1 for True, 0 for False.

---

## In summary

- `bool` is the type for truth values in Python: just `True` and `False`.
- Booleans are used for logical tests, conditions, and as the result of comparison operators.
- They work just like integers in math, where `True` is 1 and `False` is 0.
- Most special methods come from `int`, but some are defined just for `bool` to make logical operations work naturally.

---

**Tip:**  
To see everything available on `bool`, run:

```python
help(bool)
dir(bool)
```

---
