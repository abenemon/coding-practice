# Python Methods: Do They Change the Object or Not?

Some Python methods **mutate** (change) the object they're called on, while others **leave the original object unchanged** and return a new object.

---

## Methods That **Change** the Object (Mutating Methods)

*(Especially common with lists, dictionaries, and sets.)*

### **List Examples**
- `list.append(x)`        # Adds item x to the end of the list
- `list.extend(iterable)` # Adds all items from iterable to the list
- `list.insert(i, x)`     # Inserts item x at position i
- `list.remove(x)`        # Removes first occurrence of x
- `list.pop([i])`         # Removes and returns item at position i (default last)
- `list.clear()`          # Removes all items from the list
- `list.sort()`           # Sorts the list in place
- `list.reverse()`        # Reverses the list in place

### **Dictionary Examples**
- `dict.update([other])`  # Updates the dictionary with key/value pairs from other
- `dict.pop(key[, default])` # Removes and returns the value for key
- `dict.popitem()`        # Removes and returns an arbitrary key/value pair
- `dict.clear()`          # Removes all items

### **Set Examples**
- `set.add(x)`
- `set.remove(x)`
- `set.discard(x)`
- `set.pop()`
- `set.clear()`
- `set.update(iterable)`

---

## Methods That **Do Not Change** the Object (Non-mutating Methods)

*(Most string methods and many others!)*

### **String Examples**
- `str.replace(old, new)`         # Returns a new string, original is unchanged
- `str.upper()`
- `str.lower()`
- `str.capitalize()`
- `str.title()`
- `str.strip()`
- `str.split()`
- `str.join(iterable)`

### **List Examples**
- `list.count(x)`                 # Returns number of occurrences, does not change the list
- `list.index(x)`                 # Returns first index of x
- `list.copy()`                   # Returns a new (shallow) copy of the list
- `sorted(list)`                  # Returns a new sorted list (function, not method)

### **Dictionary Examples**
- `dict.get(key[, default])`
- `dict.keys()`
- `dict.values()`
- `dict.items()`
- `dict.copy()`

### **Set Examples**
- `set.union(other_set)`
- `set.intersection(other_set)`
- `set.difference(other_set)`
- `set.copy()`

---

## **How to Tell?**
- **Mutating methods** usually return `None` (they do the work in place).
- **Non-mutating methods** return a new object or a value and leave the original unchanged.
- **Strings and tuples are immutable**: all string and tuple methods return new objects, never change the original.

---

## **Why Does This Matter?**

- If you *want* to change your data in place, use mutating methods (like `list.append`).
- If you *don’t* want to accidentally overwrite your original data, use non-mutating methods or work with immutable types (like strings and tuples).

---

**Tip:**  
If you’re not sure whether a method mutates the object, check the Python documentation or try this pattern:
```python
result = obj.method()
print(result)       # If None, likely mutates in place
print(obj)          # See if the original changed
```

---

