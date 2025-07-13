# What Is an Attribute in Python?

In Python, an **attribute** is a value or method that is attached to an object.
You access attributes using dot notation, like `object.attribute`.

---

## Types of Attributes

- **Data attributes**: Store information (variables) about the object.
- **Method attributes**: Functions that belong to the object and can be called with `object.method()`.

---

## Where Do Attributes Come From?

- Attributes are defined by the object's class.
  - For example, a `Person` class might have `name` and `age` attributes.
- You can also add new attributes to objects (unless they're of a “fixed” type).

---

## Accessing Attributes

- Read an attribute: `value = obj.attribute_name`
- Set an attribute: `obj.attribute_name = new_value`
- Call a method: `obj.method_name()`

---

## Example

class Dog:
    def __init__(self, name):
        self.name = name    # 'name' is a data attribute
    def bark(self):         # 'bark' is a method attribute
        print("Woof!")

fido = Dog("Fido")
print(fido.name)        # Access data attribute → 'Fido'
fido.bark()             # Call method attribute → 'Woof!'

Here, `name` is a data attribute, and `bark` is a method attribute.

---

## Attributes vs. Dictionary Keys

- Attributes are accessed with dot notation: `obj.x`
- Dictionary keys are accessed with brackets: `d["x"]`

---

## Attributes in Built-in Objects

- Many built-in objects, like strings, lists, and NumPy arrays, have attributes.
  - Example:
    - `my_list.append` is the append method attribute of a list.
    - `arr.shape` is the shape attribute of a NumPy array.

---

## How to List Attributes

- Use the `dir()` function to see an object’s attributes: `dir(obj)`
- Use `hasattr(obj, "attribute_name")` to check if an object has an attribute.

---

## In summary

- An **attribute** is a named value or method stored inside an object.
- You access it with dot notation.
- Attributes make objects more useful, by letting them remember data and provide behaviors (methods).

---

**Tip:**
Type `help(obj)` or `dir(obj)` in Python to explore the attributes of any object!
