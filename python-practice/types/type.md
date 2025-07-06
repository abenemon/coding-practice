# Understanding Python’s `type` Class: A Natural Language Explainer

When you see `class type(object)` in Python’s help system, you’re looking at Python’s **type object**—the "metaclass" that describes what type things are, and lets you create new classes dynamically.  
This document explains what it means, how to use it, and what the special functions do, in natural language.

---

## What Is `type` in Python?

In Python, `type` is both:

1. **The function you use to check what type an object is:**  
        type("hi")        # <class 'str'>
        type([1, 2])      # <class 'list'>

2. **The metaclass that all classes are instances of:**  
   Every class in Python is itself an object of type `type`.

---

## Creating Types

- **Checking the type of an object:**  

        n = 5
        print(type(n))       # <class 'int'>

- **Dynamically creating a new type (class):**

        # type(name, bases, dict)
        MyClass = type("MyClass", (object,), {"x": 42})
        obj = MyClass()
        print(obj.x)         # 42

- **If you call `type()` with a single object, you get its type.**
- **If you call `type()` with three arguments, you dynamically make a new class.**

### Parameters

- `object`: The thing you want to know the type of.
- `name`: Name of the new type (as a string).
- `bases`: Tuple of parent classes (usually just `(object,)`).
- `dict`: Dictionary of methods and attributes for the new class.

---

## Special Methods and What They Mean

The following are some of the most important special (“dunder”) methods for `type` objects in Python.
For each, you’ll see:

- The code you usually write as a Python user.
- The special method Python uses under the hood (which you almost never type directly).
- What it means, and an example.

---

## __call__(self, *args, **kwargs)

- **What you write:**  
      instance = MyClass(5, 7)

- **What Python does:**  
      MyClass.__call__(5, 7)

- **What it means:**  
  Lets you “call” a class object (which is itself a type) to create an instance of that class.

- **Example:**

        class Dog:
            def __init__(self, name):
                self.name = name

        rex = Dog("Rex")
        # Behind the scenes: Dog.__call__("Rex")
        # rex is an instance of Dog

---

## __delattr__(self, name)

- **What you write:**  
      del MyClass.attribute

- **What Python does:**  
      MyClass.__delattr__('attribute')

- **What it means:**  
  Removes an attribute from a class.

- **Example:**

        class A:
            x = 5
        del A.x
        # Now A has no attribute 'x'

---

## __dir__(self)

- **What you write:**  
      dir(type_obj)

- **What Python does:**  
      type_obj.__dir__()

- **What it means:**  
  Lists the attributes of a type (class).

- **Example:**

        dir(int)
        # Returns list of attribute/method names

---

## __getattribute__(self, name)

- **What you write:**  
      MyClass.x

- **What Python does:**  
      MyClass.__getattribute__('x')

- **What it means:**  
  Looks up an attribute on a type (class).  
  (You rarely call this directly.)

---

## __init__(self, *args, **kwargs)

- **What you write:**  
      (Not usually called directly for type objects!)

- **What Python does:**  
      type_obj.__init__(*args, **kwargs)

- **What it means:**  
  Initializes a type object. (Usually only used by Python itself.)

---

## __instancecheck__(self, instance)

- **What you write:**  
      isinstance(obj, MyClass)

- **What Python does:**  
      MyClass.__instancecheck__(obj)

- **What it means:**  
  Checks if an object is an instance of a class (including subclasses).

- **Example:**

        isinstance(5, int)      # True

---

## __or__(self, value)

- **What you write:**  
      NewType = TypeA | TypeB

- **What Python does:**  
      TypeA.__or__(TypeB)

- **What it means:**  
  Used in Python 3.10+ for [type unions](https://peps.python.org/pep-0604/) (for type hints).

- **Example:**

        # Python 3.10+
        def foo(x: int | str):    # Equivalent to Union[int, str]
            pass

---

## __repr__(self)

- **What you write:**  
      print(type(int))

- **What Python does:**  
      type(int).__repr__()

- **What it means:**  
  Returns a string that shows how to represent the type object.

- **Example:**

        repr(type(5))      # "<class 'int'>"

---

## __ror__(self, value)

- **What you write:**  
      NewType = SomeValue | type_obj

- **What Python does:**  
      type_obj.__ror__(SomeValue)

- **What it means:**  
  Like `__or__`, but with the operands reversed.  
  Used for type unions.

---

## __setattr__(self, name, value)

- **What you write:**  
      MyClass.x = 99

- **What Python does:**  
      MyClass.__setattr__('x', 99)

- **What it means:**  
  Sets or changes a class attribute.

- **Example:**

        class C: pass
        C.a = 42

---

## __sizeof__(self)

- **What you write:**  
      size = type_obj.__sizeof__()

- **What it means:**  
  Returns the memory usage of a type object.

---

## __subclasscheck__(self, subclass)

- **What you write:**  
      issubclass(C, B)

- **What Python does:**  
      B.__subclasscheck__(C)

- **What it means:**  
  Checks if one class is a subclass of another.

- **Example:**

        class A: pass
        class B(A): pass
        issubclass(B, A)    # True

---

## __subclasses__(self)

- **What you write:**  
      MyClass.__subclasses__()

- **What it means:**  
  Returns a list of classes that directly inherit from this class.

- **Example:**

        class A: pass
        class B(A): pass
        class C(A): pass
        A.__subclasses__()      # [<class '__main__.B'>, <class '__main__.C'>]

---

## mro(self)

- **What you write:**  
      MyClass.mro()

- **What it means:**  
  Returns the "method resolution order" for a class: the order Python looks for methods and attributes.

- **Example:**

        class A: pass
        class B(A): pass
        B.mro()      # [<class '__main__.B'>, <class ']()
