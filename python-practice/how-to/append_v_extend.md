# Python List Methods: `append` vs. `extend`

Both `append` and `extend` are list methods that **add new elements** to a list—but they work differently! Knowing when and how to use each one will help you avoid common mistakes.

---

## `list.append(object)`

- **What it does:**  
  Adds its argument as a **single element** to the end of the list.
- **How it mutates:**  
  The list grows by **one new element**, regardless of what you append (even if you append another list or tuple).
- **Returns:**  
  `None` (the list itself is changed).

**Example:**
```python
lst = [1, 2, 3]
lst.append(4)
# lst is now [1, 2, 3, 4]

lst.append([5, 6])
# lst is now [1, 2, 3, 4, [5, 6]]  # [5, 6] is a single new element (a nested list)
```

---

## `list.extend(iterable)`

- **What it does:**  
  Iterates over its argument and adds **each element individually** to the end of the list.
- **How it mutates:**  
  The list grows by **as many elements as are in the iterable** you provide.
- **Returns:**  
  `None` (the list itself is changed).

**Example:**
```python
lst = [1, 2, 3]
lst.extend([4, 5])
# lst is now [1, 2, 3, 4, 5]

lst.extend((6, 7))
# lst is now [1, 2, 3, 4, 5, 6, 7]

lst.extend("ab")
# lst is now [1, 2, 3, 4, 5, 6, 7, 'a', 'b']
```

---

## **Key Differences**

| Method    | Adds argument as...           | Result with `[1, 2]` + `[3, 4]`                  | Returns |
|-----------|------------------------------|--------------------------------------------------|---------|
| `append`  | Single object (as-is)        | `[1, 2, [3, 4]]` (a nested list as one element)  | None    |
| `extend`  | Each element individually    | `[1, 2, 3, 4]` (elements added one by one)       | None    |

---

## **When to Use Each**

- Use `append` when you want to **add a single item** (could be any object, even another list as a nested item).
- Use `extend` when you want to **combine lists** or add **multiple elements** from any iterable (not nested).

---

## **Common Mistake Example**

```python
lst = [1, 2]
lst.append([3, 4])
# lst is now [1, 2, [3, 4]]  # Not [1, 2, 3, 4]!
```
**Correct way if you want [1, 2, 3, 4]:**
```python
lst = [1, 2]
lst.extend([3, 4])
# lst is now [1, 2, 3, 4]
```

---

## In summary

- `append` adds its argument as a **single item**.
- `extend` adds **each element** from its argument.
- Both **mutate** the original list and return `None`.

---

**Tip:**  
When in doubt, ask yourself:  
- “Do I want to add **one thing** (use `append`) or **several things** (use `extend`)?”

---

To see more, run:

    help(list.append)
    help(list.extend)

---
