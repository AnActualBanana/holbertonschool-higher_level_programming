# 0x0A. Python - Inheritance

This project introduces **Inheritance** in Python, a key concept in Object-Oriented Programming (OOP). It builds upon previous lessons about classes and objects by exploring how to create class hierarchies, override methods, and use built-in functions like `isinstance()` and `issubclass()`.

---

## 📚 Learning Objectives

- Understand what inheritance is and how to use it.
- Know how to override a method or attribute inherited from the parent class.
- Use built-in functions like `isinstance()` and `issubclass()`.
- Understand the difference between a class and an object.
- Explore Python’s `dir()` function and how to dynamically inspect objects.

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `0-lookup.py` | Function that returns the list of available attributes and methods of an object. |
| `1-my_list.py` | Class that inherits from `list`, with a method to print a sorted list. |
| `2-is_same_class.py` | Function that checks if an object is exactly an instance of a specified class. |
| `3-is_kind_of_class.py` | Function that checks if an object is an instance of, or inherits from, a specified class. |
| `4-inherits_from.py` | Function that checks if an object is a subclass (but not the same class) of a specified class. |
| `5-base_geometry.py` | Empty class `BaseGeometry`. |
| `6-base_geometry.py` | Class `BaseGeometry` with a `area()` method (not implemented) and integer validation. |
| `7-base_geometry.py` | Same as above, but with full docstrings. |
| `8-rectangle.py` | Class `Rectangle` that inherits from `BaseGeometry`. |
| `9-rectangle.py` | Class `Rectangle` with `area()` method and `__str__` method for printing. |
| `10-square.py` | Class `Square` that inherits from `Rectangle`. |
| `11-square.py` | Class `Square` with `area()` method and print representation. |

---

## 🧪 Tests

Unit tests are included in the `tests/` folder and can be run using:

```bash
python3 -m unittest discover tests
```

## Author
Logan McClain
