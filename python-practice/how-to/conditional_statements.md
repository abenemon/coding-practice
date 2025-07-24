# Understanding Conditional Statements in Python: A Natural Language Explainer

Conditional statements are how you make decisions in Python code—telling the program, “Do this only if something is true.”

## What Is a Conditional Statement?

- A conditional statement checks whether something (an “expression”) is true or false.
- Based on the result, Python chooses which lines of code to run.
- The most common conditional is the `if` statement, with optional `elif` (“else if”) and `else` parts.

## Basic Structure

- **What you write:**
    ```python
    if condition:
        # code to run if condition is True
    ```
- **What Python does:**
    - Checks the `condition`.
    - If it’s `True`, runs the indented code.
    - If it’s `False`, skips that code.

## Extended Structure with `elif` and `else`

- **What you write:**
    ```python
    if condition1:
        # code if condition1 is True
    elif condition2:
        # code if condition2 is True
    else:
        # code if neither is True
    ```
- **What Python does:**
    - Tests each condition in order.
    - Runs the first block where the condition is `True`.
    - If none match, runs the `else` block.

## Examples

- **Simple if:**
    ```python
    x = 5
    if x > 0:
        print("x is positive")
    ```
- **If-else:**
    ```python
    x = -2
    if x >= 0:
        print("Non-negative")
    else:
        print("Negative")
    ```
- **If-elif-else:**
    ```python
    score = 85
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    else:
        print("Grade: C or below")
    ```

## The Condition

- The “condition” can be any expression that evaluates to `True` or `False`.
- Common comparisons:
    - `==` (equal to)
    - `!=` (not equal to)
    - `<`, `>`, `<=`, `>=`
    - You can combine with `and`, `or`, `not`
- Examples:
    - `x == 10`
    - `age >= 18 and age < 65`
    - `not is_raining`

## Indentation Matters

- All code blocks under `if`, `elif`, or `else` must be indented (usually 4 spaces).
- This tells Python which statements belong to each branch.

## Quick Reference Table

| Statement      | Runs when...                          |
|----------------|--------------------------------------|
| `if`           | The condition is `True`               |
| `elif`         | All previous conditions were `False`, and this one is `True` |
| `else`         | All previous conditions were `False`  |

## Common Mistakes

- Forgetting the colon (`:`) after `if`, `elif`, or `else`
- Not indenting the code block under each branch
- Using `=` instead of `==` for comparison

## In Summary

- Conditional statements let your code make choices.
- Use `if`, `elif`, and `else` to control what happens based on conditions.
- Indentation and colons are critical for syntax.
- Test conditions with comparisons or logical operators.

**Tip:**  
You can nest conditionals for more complex decisions, but keep code readable!