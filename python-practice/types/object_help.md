# Understanding Python’s `object` Class: A Natural Language Explainer

When you see `class object` in Python’s help system, you’re looking at Python’s **base class**—the most basic type from which every other Python class inherits (directly or indirectly).

---

## What Is `object` in Python?

- `object` is the root of all classes in Python.
- Every user-defined class implicitly inherits from `object` (unless you use old-style classes in Python 2).
- If you call `object()`, you get a plain, featureless object.

    empty_thing = object()

You can’t add attributes to a plain `object` instance; it’s a “blank slate.”

---

## Creating Objects

- **Default usage:**

        x = object()

- **As a base class:**

        class Foo(object):
            pass

        y = Foo()

---

## Special Methods and What They Mean

These are the “dunder” methods (`__something__`) you see if you run `help(object)`.  
Below, you’ll find what you write, what Python does, what it means, and an example.

---

## __delattr__(self, name)

- **What you write:**  
    `del obj.attr`

- **What Python does:**  
    `obj.__delattr__('attr')`

- **What it means:**  
    Deletes an attribute from an object.  
    (You can only use this if the object supports attributes.)

- **Example:**

        class Foo:
            x = 5
        f = Foo()
        del f.x

---

## __dir__(self)

- **What you write:**  
    `dir(obj)`

- **What Python does:**  
    `obj.__dir__()`

- **What it means:**  
    Lists the attributes and methods of the object.

- **Example:**

        dir(object())
        # Shows all default attributes and methods

---

## __eq__(self, value)

- **What you write:**  
    `a == b`

- **What Python does:**  
    `a.__eq__(b)`

- **What it means:**  
    Checks if two objects are equal.

- **Example:**

        object() == object()      # False (different objects)

---

## __format__(self, format_spec)

- **What you write:**  
    `"{}".format(obj)`

- **What Python does:**  
    `obj.__format__(format_spec)`

- **What it means:**  
    Default object formatting; calls `str(obj)` if `format_spec` is empty.

- **Example:**

        "{}".format(object())   # Usually something like "<object object at 0x...>"

---

## __ge__(self, value)

- **What you write:**  
    `a >= b`

- **What Python does:**  
    `a.__ge__(b)`

- **What it means:**  
    Checks if one object is greater than or equal to another (default raises an error unless you define it).

---

## __getattribute__(self, name)

- **What you write:**  
    `obj.attr`

- **What Python does:**  
    `obj.__getattribute__('attr')`

- **What it means:**  
    Retrieves an attribute from the object.

- **Example:**

        class Bar:
            x = 10
        b = Bar()
        b.x
        # or
        b.__getattribute__('x')

---

## __getstate__(self)

- **What you write:**  
    (Used for pickling—saving objects.)

- **What Python does:**  
    `obj.__getstate__()`

- **What it means:**  
    Returns the state of the object for serialization.

---

## __gt__(self, value)

- **What you write:**  
    `a > b`

- **What Python does:**  
    `a.__gt__(b)`

- **What it means:**  
    Checks if one object is greater than another (default raises error unless defined).

---

## __hash__(self)

- **What you write:**  
    `hash(obj)`

- **What Python does:**  
    `obj.__hash__()`

- **What it means:**  
    Returns a number representing the object (for using it in sets, dicts).

- **Example:**

        hash(object())

---

## __init__(self, *args, **kwargs)

- **What you write:**  
    `obj = MyClass()`

- **What Python does:**  
    `obj.__init__(*args, **kwargs)`

- **What it means:**  
    Initializes a new object.

- **Example:**

        class Foo:
            def __init__(self):
                print("I am born!")

---

## __le__(self, value)

- **What you write:**  
    `a <= b`

- **What Python does:**  
    `a.__le__(b)`

- **What it means:**  
    Checks if one object is less than or equal to another (default raises error).

---

## __lt__(self, value)

- **What you write:**  
    `a < b`

- **What Python does:**  
    `a.__lt__(b)`

- **What it means:**  
    Checks if one object is less than another (default raises error).

---

## __ne__(self, value)

- **What you write:**  
    `a != b`

- **What Python does:**  
    `a.__ne__(b)`

- **What it means:**  
    Checks if two objects are NOT equal.

- **Example:**

        object() != object()    # True

---

## __reduce__(self), __reduce_ex__(self, protocol)

- **What you write:**  
    (Used by the pickle module.)

- **What it means:**  
    Helps Python serialize (pickle) objects.

---

## __repr__(self)

- **What you write:**  
    `repr(obj)`

- **What Python does:**  
    `obj.__repr__()`

- **What it means:**  
    Returns a string for representing the object (usually for debugging).

- **Example:**

        repr(object())     # "<object object at 0x...>"

---

## __setattr__(self, name, value)

- **What you write:**  
    `obj.attr = value`

- **What Python does:**  
    `obj.__setattr__('attr', value)`

- **What it means:**  
    Sets an attribute on the object.

- **Example:**

        class Q:
            pass
        q = Q()
        q.x = 7
        # or
        q.__setattr__('x', 7)

---

## __sizeof__(self)

- **What you write:**  
    `obj.__sizeof__()`

- **What it means:**  
    Returns the size of the object in memory (in bytes).

---

## __str__(self)

- **What you write:**  
    `str(obj)`
    `print(obj)`

- **What Python does:**  
    `obj.__str__()`

- **What it means:**  
    Returns a user-friendly string for the object.

- **Example:**

        print(object())     # <object object at 0x...>

---

## Class methods

### __init_subclass__()

- **What you write:**  
    (Defines how subclasses of a class are initialized.)

- **What it means:**  
    Lets you customize behavior when your class is subclassed.

---

### __subclasshook__(object)

- **What you write:**  
    (Used in advanced subclass checks, especially with ABCs.)

- **What it means:**  
    Lets you customize how `issubclass()` works for your class.

---

## Static methods

### __new__(*args, **kwargs)

- **What you write:**  
    (Called to create a new object before `__init__`.)

- **What it means:**  
    Allocates and returns a new object instance.

---

## Data and other attributes

- **__class__**  
    - The class of this object (e.g. `type(object())` is `<class 'object'>`).

---

## In summary

- `object` is the root of all Python classes.
- All new-style classes (in Python 3, that's all classes) inherit from `object`.
- It provides basic methods for comparison, hashing, attribute access, and introspection.
- You almost never use `object` directly, but all your classes are built on top of it!

---

**Tip:**  
To see everything available on `object`, run:

    help(object)
    dir(object)

---

Feel free to copy and save this file in your GitHub repo!
