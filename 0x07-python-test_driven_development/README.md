# 0x07. Python - Test-Driven Development

This project introduces **Test-Driven Development (TDD)** in Python, emphasizing writing tests before actual implementation. It also highlights the importance of documentation and edge case handling in writing robust and reliable functions.

---

## 📚 Learning Objectives

By the end of this project, you should be able to:

- Understand the importance of documentation
- Understand the importance of testing
- Know how to write unit tests using `doctest` and `unittest`
- Know the difference between unit tests and integration tests
- Apply the TDD approach to coding

---

## 📁 Project Structure

| File                        | Description |
|-----------------------------|-------------|
| `0-add_integer.py`          | Adds two integers or floats. Raises `TypeError` if inputs are invalid. |
| `0-main.py`                 | Test script for `0-add_integer.py`. |
| `2-matrix_divided.py`       | Divides all elements of a matrix. Includes input validations. |
| `2-main.py`                 | Test script for `2-matrix_divided.py`. |
| `3-say_my_name.py`          | Prints `My name is <first name> <last name>`. Validates string input. |
| `3-main.py`                 | Test script for `3-say_my_name.py`. |
| `4-print_square.py`         | Prints a square of `#` with the given size. Validates input. |
| `4-main.py`                 | Test script for `4-print_square.py`. |
| `5-text_indentation.py`     | Prints text with two new lines after `.`, `?`, and `:`. |
| `5-main.py`                 | Test script for `5-text_indentation.py`. |
| `tests/`                    | Folder containing unit tests written using the `doctest` module. |
| `__pycache__/`              | Directory for cached bytecode files. |

---

## 🧪 Testing

### Using `doctest`

Each Python file includes embedded tests in the docstrings. To run them:

```bash
python3 -m doctest -v <filename>.py
```

## Author
Logan McClain
