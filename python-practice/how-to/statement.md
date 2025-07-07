# Common Statements in Python: A Natural Language Guide

In Python, a **statement** is an instruction that the interpreter can execute.  
Statements control what your code does—assign values, make decisions, repeat actions, define functions, and more.

---

## Major Types of Python Statements

Here are the most common Python statements, with a quick summary of what each one does:

---

### 1. Assignment Statement

- **What you write:**  
    `x = 5`  
    `name = "Alice"`

- **What it does:**  
    Stores a value in a variable.

---

### 2. Import Statement

- **What you write:**  
    `import math`  
    `from sys import argv`

- **What it does:**  
    Brings in modules or parts of modules so you can use them.

---

### 3. def Statement

- **What you write:**  
    `def greet(name):`
- **What it does:**  
    Defines a new function.

---

### 4. class Statement

- **What you write:**  
    `class Dog:`
- **What it does:**  
    Defines a new class (your own object type).

---

### 5. if Statement

- **What you write:**  
    `if age > 18:`
- **What it does:**  
    Runs code only if a condition is true.

---

### 6. elif / else Statement

- **What you write:**  
    `elif x < 0:`  
    `else:`
- **What it does:**  
    Adds extra conditions or a default action to an `if` statement.

---

### 7. for Statement

- **What you write:**  
    `for item in collection:`
- **What it does:**  
    Loops over items in a sequence.

---

### 8. while Statement

- **What you write:**  
    `while x > 0:`
- **What it does:**  
    Loops as long as a condition is true.

---

### 9. try / except / finally Statement

- **What you write:**  
    `try: ... except: ... finally: ...`
- **What it does:**  
    Handles errors (exceptions) that might occur.

---

### 10. with Statement

- **What you write:**  
    `with open("file.txt") as f:`
- **What it does:**  
    Sets up and cleans up resources automatically (context manager).

---

### 11. return Statement

- **What you write:**  
    `return x + y`
- **What it does:**  
    Sends a value back from a function.

---

### 12. yield Statement

- **What you write:**  
    `yield x`
- **What it does:**  
    Produces a value from a generator function.

---

### 13. pass Statement

- **What you write:**  
    `pass`
- **What it does:**  
    Does nothing (a placeholder).

---

### 14. break Statement

- **What you write:**  
    `break`
- **What it does:**  
    Exits a loop immediately.

---

### 15. continue Statement

- **What you write:**  
    `continue`
- **What it does:**  
    Skips to the next iteration of a loop.

---

### 16. global Statement

- **What you write:**  
    `global x`
- **What it does:**  
    Declares that `x` is a global variable.

---

### 17. nonlocal Statement

- **What you write:**  
    `nonlocal y`
- **What it does:**  
    Declares that `y` is not local, but comes from an enclosing function.

---

### 18. assert Statement

- **What you write:**  
    `assert x > 0`
- **What it does:**  
    Checks if a condition is true—if not, raises an error.

---

### 19. del Statement

- **What you write:**  
    `del x`
- **What it does:**  
    Deletes a variable, item, or attribute.

---

### 20. raise Statement

- **What you write:**  
    `raise ValueError("Oops!")`
- **What it does:**  
    Raises an exception (an error on purpose).

---

## Other Statements

- **async / await** (for asynchronous programming)
- **lambda** (for creating anonymous functions, technically an expression, but used like a statement)

---

## In summary

- Python has many statements for control flow, assignment, loops, function/class definition, error handling, and more.
- Statements are the building blocks of your Python programs.

---

**Tip:**  
You can see all Python keywords (many of which are statements) by running:

    import keyword
    print(keyword.kwlist)

---
