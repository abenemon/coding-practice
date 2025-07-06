# Understanding Python’s `int` Class: A Natural Language Explainer

When you see `class int(object)` in Python’s help system, you’re looking at Python’s **integer** type—a type for whole numbers (like 1, -3, 42).

---

## What Is `int` in Python?

- `int` stands for integer numbers in Python.
- Examples:

        age = 42
        temperature = -7
        count = 0

- You get an `int` any time you write a number without a decimal, or when you convert something to an integer.

---

## Creating Integers

- **Typing a whole number:**  
      `n = 7`

- **Converting another type to int:**  
      `n = int("123")`          # 123  
      `n = int(4.2)`            # 4 (truncates towards zero)  
      `n = int("0b101", 2)`     # 5 (from binary string)

- **Empty int:**  
      `n = int()`               # 0

### Parameters

- `x` (optional): The value to convert to int.  
- `base` (optional): Base for converting a string (2 for binary, 8 for octal, 16 for hex, etc.).

---

## Special Methods and What They Mean

These are the “dunder” methods (`__something__`) used behind the scenes for math, comparisons, and other operations on integers.

---

## __abs__(self)

- **What you write:**  
    `abs(x)`

- **What Python does:**  
    `x.__abs__()`

- **What it means:**  
    Returns the absolute value (removes any minus sign).

- **Example:**  
    `abs(-5)`    # 5

---

## __add__(self, value)

- **What you write:**  
    `x + y`

- **What Python does:**  
    `x.__add__(y)`

- **What it means:**  
    Adds two integers.

- **Example:**  
    `3 + 4`    # 7

---

## __and__(self, value)

- **What you write:**  
    `x & y`

- **What Python does:**  
    `x.__and__(y)`

- **What it means:**  
    Bitwise AND operation (works at the binary level).

- **Example:**  
    `5 & 3`    # 1 (since 0b101 & 0b011 == 0b001)

---

## __bool__(self)

- **What you write:**  
    `bool(x)`

- **What Python does:**  
    `x.__bool__()`

- **What it means:**  
    Returns `False` if the integer is 0, `True` otherwise.

- **Example:**  
    `bool(0)`    # False  
    `bool(42)`   # True

---

## __ceil__(self)

- **What you write:**  
    `math.ceil(x)`

- **What Python does:**  
    `x.__ceil__()`

- **What it means:**  
    Returns itself (for compatibility with float/decimal).  
    For an integer, ceiling is itself.

- **Example:**  
    `import math; math.ceil(7)`    # 7

---

## __divmod__(self, value)

- **What you write:**  
    `divmod(x, y)`

- **What Python does:**  
    `x.__divmod__(y)`

- **What it means:**  
    Returns `(x // y, x % y)` (quotient and remainder).

- **Example:**  
    `divmod(10, 3)`    # (3, 1)

---

## __eq__(self, value)

- **What you write:**  
    `x == y`

- **What Python does:**  
    `x.__eq__(y)`

- **What it means:**  
    Checks if two integers are equal.

- **Example:**  
    `4 == 4`   # True  
    `2 == 3`   # False

---

## __float__(self)

- **What you write:**  
    `float(x)`

- **What Python does:**  
    `x.__float__()`

- **What it means:**  
    Converts the integer to a float.

- **Example:**  
    `float(7)`    # 7.0

---

## __floor__(self)

- **What you write:**  
    `math.floor(x)`

- **What Python does:**  
    `x.__floor__()`

- **What it means:**  
    Returns itself (for compatibility with float/decimal).

---

## __floordiv__(self, value)

- **What you write:**  
    `x // y`

- **What Python does:**  
    `x.__floordiv__(y)`

- **What it means:**  
    Floor division: divides and rounds down to the nearest whole number.

- **Example:**  
    `7 // 2`    # 3

---

## __format__(self, format_spec)

- **What you write:**  
    `"{:04d}".format(x)`

- **What Python does:**  
    `x.__format__(format_spec)`

- **What it means:**  
    Formats the integer as a string according to the format specifier.

- **Example:**  
    `"{:04d}".format(5)`   # "0005"

---

## __ge__(self, value)

- **What you write:**  
    `x >= y`

- **What Python does:**  
    `x.__ge__(y)`

- **What it means:**  
    Checks if one integer is greater than or equal to another.

- **Example:**  
    `5 >= 3`    # True

---

## __getattribute__(self, name)

- **What you write:**  
    `x.real`

- **What Python does:**  
    `x.__getattribute__('real')`

- **What it means:**  
    Looks up an attribute on the integer.

---

## __getnewargs__(self)

- **What you write:**  
    (Internal—used for pickling)

- **What it means:**  
    Returns arguments needed to reconstruct the integer.

---

## __gt__(self, value)

- **What you write:**  
    `x > y`

- **What Python does:**  
    `x.__gt__(y)`

- **What it means:**  
    Checks if one integer is greater than another.

- **Example:**  
    `7 > 3`    # True

---

## __hash__(self)

- **What you write:**  
    `hash(x)`

- **What Python does:**  
    `x.__hash__()`

- **What it means:**  
    Returns a hash value for the integer (so it can be used as a dictionary key).

---

## __index__(self)

- **What you write:**  
    `lst[x]` (when `x` is an int)

- **What Python does:**  
    `x.__index__()`

- **What it means:**  
    Used for converting the int to an integer index (for slicing, etc).

---

## __int__(self)

- **What you write:**  
    `int(x)`

- **What Python does:**  
    `x.__int__()`

- **What it means:**  
    Returns itself.

---

## __invert__(self)

- **What you write:**  
    `~x`

- **What Python does:**  
    `x.__invert__()`

- **What it means:**  
    Bitwise NOT (inverts all bits in the number).

- **Example:**  
    `~2`   # -3

---

## __le__(self, value)

- **What you write:**  
    `x <= y`

- **What Python does:**  
    `x.__le__(y)`

- **What it means:**  
    Checks if one integer is less than or equal to another.

- **Example:**  
    `3 <= 3`    # True

---

## __lshift__(self, value)

- **What you write:**  
    `x << y`

- **What Python does:**  
    `x.__lshift__(y)`

- **What it means:**  
    Shifts the bits of `x` to the left by `y` places.

- **Example:**  
    `3 << 2`    # 12 (0b11 << 2 == 0b1100)

---

## __lt__(self, value)

- **What you write:**  
    `x < y`

- **What Python does:**  
    `x.__lt__(y)`

- **What it means:**  
    Checks if one integer is less than another.

- **Example:**  
    `2 < 4`    # True

---

## __mod__(self, value)

- **What you write:**  
    `x % y`

- **What Python does:**  
    `x.__mod__(y)`

- **What it means:**  
    Returns the remainder of `x` divided by `y`.

- **Example:**  
    `10 % 3`    # 1

---

## __mul__(self, value)

- **What you write:**  
    `x * y`

- **What Python does:**  
    `x.__mul__(y)`

- **What it means:**  
    Multiplies two integers.

- **Example:**  
    `3 * 4`    # 12

---

## __ne__(self, value)

- **What you write:**  
    `x != y`

- **What Python does:**  
    `x.__ne__(y)`

- **What it means:**  
    Checks if two integers are NOT equal.

---

## __neg__(self)

- **What you write:**  
    `-x`

- **What Python does:**  
    `x.__neg__()`

- **What it means:**  
    Returns the negation of the integer.

- **Example:**  
    `-7`    # -7

---

## __or__(self, value)

- **What you write:**  
    `x | y`

- **What Python does:**  
    `x.__or__(y)`

- **What it means:**  
    Bitwise OR.

- **Example:**  
    `5 | 2`   # 7

---

## __pos__(self)

- **What you write:**  
    `+x`

- **What Python does:**  
    `x.__pos__()`

- **What it means:**  
    Returns itself.

---

## __pow__(self, value, mod=None)

- **What you write:**  
    `x ** y`  
    `pow(x, y, mod)`

- **What Python does:**  
    `x.__pow__(y, mod)`

- **What it means:**  
    Raises x to the power y (optionally modulo another number).

- **Example:**  
    `2 ** 3`      # 8  
    `pow(2, 3, 5)`  # 3

---

## __radd__, __rsub__, __rmul__, etc.

- **What you write:**  
    `y + x`, `y - x`, etc. (where x is int and y is something else)

- **What Python does:**  
    `x.__radd__(y)`, etc.

- **What it means:**  
    Lets Python handle cases where the left side isn't an int, but the right side is.

---

## __repr__(self)

- **What you write:**  
    `repr(x)`

- **What Python does:**  
    `x.__repr__()`

- **What it means:**  
    Returns a string for representing the integer in code.

---

## __sizeof__(self)

- **What you write:**  
    `x.__sizeof__()`

- **What it means:**  
    Returns the size of the int object in memory (in bytes).

---

## __str__(self)

- **What you write:**  
    `str(x)`

- **What Python does:**  
    `x.__str__()`

- **What it means:**  
    Returns the string version of the integer.

- **Example:**  
    `str(42)`    # "42"

---

## Methods unique to int

---

### as_integer_ratio(self)

- **What you write:**  
    `x.as_integer_ratio()`

- **What it means:**  
    Returns a tuple `(numerator, denominator)` for the integer as a fraction.

- **Example:**  
    `(10).as_integer_ratio()`    # (10, 1)

---

### bit_count(self)

- **What you write:**  
    `x.bit_count()`

- **What it means:**  
    Returns how many 1-bits are in the integer’s binary form.

- **Example:**  
    `(13).bit_count()`   # 3 (since 13 is 0b1101)

---

### bit_length(self)

- **What you write:**  
    `x.bit_length()`

- **What it means:**  
    Number of bits needed to represent the integer in binary.

- **Example:**  
    `(37).bit_length()`  # 6 (since 37 is 0b100101)

---

### conjugate(self)

- **What you write:**  
    `x.conjugate()`

- **What it means:**  
    Returns itself (for compatibility with complex numbers).

---

### is_integer(self)

- **What you write:**  
    `x.is_integer()`

- **What it means:**  
    Always returns True (for compatibility with floats).

---

### to_bytes(self, length=1, byteorder='big', signed=False)

- **What you write:**  
    `x.to_bytes(length, byteorder, signed=False)`

- **What it means:**  
    Returns a bytes object representing the integer.

- **Example:**  
    `(255).to_bytes(2, 'big')`   # b'\x00\xff'

---

### from_bytes(bytes, byteorder='big', signed=False) (class method)

- **What you write:**  
    `int.from_bytes(b, 'big')`

- **What it means:**  
    Converts a bytes object to an integer.

- **Example:**  
    `int.from_bytes(b'\x00\xff', 'big')`   # 255

---

## Data descriptors

- **denominator**: Always 1 for integers.
- **imag**: Always 0 (for complex compatibility).
- **numerator**: The integer itself.
- **real**: The integer itself.

---

## In summary

- `int` is the type for whole numbers in Python.
- It supports all basic math, comparisons, bitwise operations, and conversions.
- You use it all the time, even if you never call these dunder methods directly.

---

**Tip:**  
To see everything available on `int`, run:

    help(int)
    dir(int)

---

Feel free to copy and save this file in your GitHub repo!
