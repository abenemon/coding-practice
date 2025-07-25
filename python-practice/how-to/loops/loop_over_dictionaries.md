# Looping Over Dictionaries: Printing Keys and Values with `.items()`

In Python, dictionaries store data as pairs: **keys** (like country names) and **values** (like population numbers). When you want to print each key and its corresponding value, you can't just write `for k, v in my_dict:`—that will cause an error! Instead, you need the `.items()` method.

---

## Example Dictionary

    world = { "afghanistan":30.55, 
              "albania":2.77,
              "algeria":39.21 }

---

## What NOT To Do

    for k, v in world:
          print(k, v)

- This gives an error because iterating over a dictionary by default only gives you the keys, not key-value pairs.
- Python expects one variable per iteration (the key), but you provided two.

---

## The Correct Way: Using `.items()`

    for key, value in world.items():
          print(key + " -- " + str(value))

- `.items()` gives you each **(key, value)** pair in the dictionary for every loop.
- You can name the variables anything (like `k, v`), but the **order matters**: first is always the key, second is always the value.
- Each pair can be used directly in your print statement or for any processing.

---

## Sample Output

    afghanistan -- 30.55
    albania -- 2.77
    algeria -- 39.21

---

## Important Notes

- **Order is not guaranteed**: Especially in older Python versions (before 3.7), dictionaries are **unordered**, so the printout order may differ from the way you wrote the dictionary.
- From Python 3.7 onward, dictionaries **remember insertion order**—but you should not rely on this for earlier versions.

---

## Summary

- To loop over both keys and values in a dictionary, use `.items()`.
- Don't forget: `for key, value in my_dict.items():`
- Variable names can be anything, but their positions (key first, value second) matter.
- Output order may not match the order you defined the dictionary (unless using Python 3.7+).

---
