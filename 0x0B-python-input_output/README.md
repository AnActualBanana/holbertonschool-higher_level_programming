# 0x0B. Python - Input/Output

This project dives into Python's powerful file I/O capabilities, working with both text and JSON data. It introduces reading, writing, appending to files, and serializing/deserializing Python objects using JSON.

---

## 📚 Learning Objectives

- How to open, read, and write files in Python.
- How to use `with` for file handling.
- Understanding file modes (`r`, `w`, `a`).
- How to convert Python data structures to JSON and vice versa.
- Understand `json.dumps()`, `json.loads()`, `json.dump()`, and `json.load()`.
- How to work with classes and customize JSON serialization.

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `0-read_file.py` | Reads a text file and prints its contents to stdout. |
| `1-write_file.py` | Writes a string to a text file and returns the number of characters written. |
| `2-append_write.py` | Appends a string to a text file and returns the number of characters added. |
| `3-to_json_string.py` | Converts a Python object to a JSON string. |
| `4-from_json_string.py` | Converts a JSON string to a Python object. |
| `5-save_to_json_file.py` | Saves a Python object to a file in JSON format. |
| `6-load_from_json_file.py` | Loads a Python object from a JSON file. |
| `7-add_item.py` | Adds command-line arguments to a Python list and saves them to a JSON file. |
| `8-class_to_json.py` | Converts an instance of a class to a dictionary for JSON serialization. |
| `9-student.py` | Defines a `Student` class with a method to convert to JSON. |
| `10-student.py` | Adds ability to create `Student` from JSON dictionary. |
| `11-student.py` | `Student` class with conditional dictionary filtering for serialization. |
| `12-pascal_triangle.py` | Returns a list of lists representing Pascal’s Triangle of a given size. |

---

## 🧪 Tests

Use the provided `main.py` files to test each module:

```bash
python3 0-main.py
python3 1-main.py
```

## Author
Logan McClain
