# Python Basics Explained

## Types

**Types** are the “kinds of things” Python can work with—think of them like categories for your data.

- `str()` – **String**  
  A sequence of letters, numbers, or symbols, usually used for text.  
  Example: `"hello"`, `"2024-07-05"`

- `list()` – **List**  
  An *ordered* collection of items. You can change, add, or remove things in a list.  
  Example: `[1, 2, 3]`, `["apple", "banana", "pear"]`

- `int()` – **Integer**  
  A whole number, with no decimal point.  
  Example: `5`, `-42`, `2024`

- `float()` – **Floating-point number**  
  A number that *can* have a decimal point.  
  Example: `3.14`, `0.0`, `-7.5`

**Why do types matter?**  
Each type allows you to do different things. You can add numbers, but you can’t add a number and a string without converting.

---

## Functions

**Functions** are built-in “mini-programs” in Python you can use to do something—just call them with parentheses.

- `type(x)` – Shows you the *type* of `x`.  
  ```python
  print(type("hello"))  # <class 'str'>
  print(type(5))        # <class 'int'>
  ```

- `print(x)` – Sends information to your screen.  
  ```python
  print("Hello, world!")
  ```

- `max(a, b, c, ...)` – Gives you the *largest* value.  
  ```python
  print(max(1, 5, 3))  # 5
  ```

- `round(x, n)` – Rounds a number to `n` decimal places.  
  ```python
  print(round(3.14159, 2))  # 3.14
  ```

- `help(x)` – Opens up the help/documentation for anything in Python.  
  ```python
  help(str)
  ```

- `len(x)` – Tells you how many items are in something (like a list or string).  
  ```python
  print(len("hello"))    # 5
  print(len([1,2,3]))    # 3
  ```

- `sorted(x)` – Returns a sorted version of your list (doesn’t change the original).  
  ```python
  numbers = [3, 1, 2]
  print(sorted(numbers))  # [1, 2, 3]
  ```

---

## Methods

**Methods** are like functions, but you use them *on* a specific object (like a string or a list), with a dot: `thing.method()`.

- `.append(y)` – Adds `y` to the end of a list.  
  ```python
  my_list = [1, 2, 3]
  my_list.append(4)
  print(my_list)  # [1, 2, 3, 4]
  ```

- `.replace(a, b)` – In a string, replaces every occurrence of `a` with `b`.  
  ```python
  text = "Hello world"
  print(text.replace("world", "Python"))  # "Hello Python"
  ```

- `.upper()` – Makes all letters in a string uppercase.  
  ```python
  name = "abe"
  print(name.upper())  # "ABE"
  ```

- `.reverse()` – Flips the order of a list, changing it in-place.  
  ```python
  nums = [1, 2, 3]
  nums.reverse()
  print(nums)  # [3, 2, 1]
  ```

---

**Bottom line:**  
- **Types** are what your data “is.”
- **Functions** are tools you use on any data.
- **Methods** are tools that belong to a particular kind of data (like a string or a list).

If you want even **more explanation, analogies, or practice problems** for any of these, just tell me what’s confusing or what you’d like to try!

# Basic Math with Python

## Addition, subtraction
    
    `print(5 + 5)`
    `print(5 - 5)`

## Multiplication, division, modulo, and exponentiation
    
    `print(3 * 5)`
    `print(10 / 2)`
    `print(18 % 7)`
    `print(4 ** 2)`

## How much is your $100 worth after 7 years?
    
    `print(100 * (1.1**7))`
