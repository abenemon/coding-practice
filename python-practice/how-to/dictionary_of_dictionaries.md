# Understanding the Dictionary of Dictionaries Pattern in Python

A **dictionary of dictionaries** is a common way in Python to organize complex, hierarchical data. This structure lets you store dictionaries as the values inside another dictionary, making it easy to group related data under a single key.

## What Is a Dictionary of Dictionaries?

- The **outer dictionary** maps keys to inner dictionaries.
- Each **inner dictionary** holds additional key-value pairs related to its parent key.
- Useful for representing real-world entities with multiple attributes (like countries with capital and population).

## Example

Suppose you want to store information about several European countries, including their capital city and population. Here’s how you’d do it with a dictionary of dictionaries:

``europe = { 
    'spain':   { 'capital': 'madrid',  'population': 46.77 },
    'france':  { 'capital': 'paris',   'population': 66.03 },
    'germany': { 'capital': 'berlin',  'population': 80.62 },
    'norway':  { 'capital': 'oslo',    'population': 5.084 }
}``

## Accessing Data

You can get an inner dictionary by using the outer key:

``europe['france']``  
# Returns: ``{'capital': 'paris', 'population': 66.03}``

You can then access a specific attribute:

``europe['france']['capital']``  
# Returns: ``'paris'``

## Adding or Updating Entries

- **Add a new country:**
  ``europe['italy'] = { 'capital': 'rome', 'population': 59.83 }``

- **Update an existing value:**
  ``europe['germany']['population'] = 81.00``

## Looping Through a Dictionary of Dictionaries

To print out all countries and their capitals:

``for country, info in europe.items():
    print(country, "->", info['capital'])``

## Why Use This Pattern?

- Keeps related information grouped under one top-level key.
- Makes it easy to look up, add, or modify complex records.
- Works well for tabular data, configuration settings, or any nested data structure.

## In Summary

* A dictionary of dictionaries is a powerful way to represent structured data.
* Access data with double indexing: ``outer_dict[key1][key2]``.
* Supports easy updates, lookups, and iterations.

Tip: This pattern is widely used in real projects—mastering it will help you manage more complex data in your Python code!
