# 0x09. Python - Almost a Circle

This project is part of the Higher-Level Programming curriculum. It is designed to reinforce concepts of object-oriented programming in Python through the creation of a simple class hierarchy that models geometric shapes. It also incorporates principles like PEP8 style guidelines, unit testing, serialization/deserialization with JSON, and file I/O.

## Description

This project defines two classes, `Base`, `Rectangle`, and `Square`, to demonstrate OOP principles and provide a foundation for working with JSON file serialization and object manipulation in Python. The main goal is to build a fully functioning model of geometry classes that handle their own persistence.

## Project Structure


📁 Files
<details> <summary><code>models/</code> — Class definitions and base logic</summary>
base.py — The base class that manages ID assignment and handles JSON serialization/deserialization

rectangle.py — Inherits from Base, defines a Rectangle with width, height, x, y

square.py — Inherits from Rectangle, defines a Square with size

</details> <details> <summary>🧪 Main test files — Each corresponds to a specific task or set of tasks</summary>
0-main.py — Initial tests for Base class and tasks 0, 1

1-main.py — Tests for task 2

2-main.py — Debugging

3-main.py — Debugging

4-main.py — Tasks up to 6, fixed indentation issues

5-main.py — Continuation of task 6 fixes

6-main.py — Task 7

7-main.py — Task 8

8-main.py — Task 9

9-main.py — Task 11

10-main.py — Task 11 (continued or different implementation)

11-main.py — Task 12

12-main.py — Task 13

13-main.py — Task 14

14-main.py — Task 15

15-main.py — Final recheck

</details>
README.md — Project documentation

## Features

- Inheritance and class relationships (`Rectangle` inherits from `Base`, `Square` inherits from `Rectangle`)
- Encapsulation of attributes with getters/setters
- Data validation (e.g., checking for integers and positive values)
- Serialization and deserialization to/from JSON
- File I/O for saving and loading objects
- PEP8 style compliance
- Unit testing (not shown here, but can be added for completeness)

## Usage

You can run the test files to observe the behavior of the different tasks:

```bash
python3 0-main.py
python3 1-main.py
...
python3 15-main.py
```

## Author
Logan McClain
