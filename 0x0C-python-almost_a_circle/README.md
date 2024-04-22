# Project: 0x0C. Python - Almost a circle
This project aims to implement a set of classes in Python to manage geometric shapes such as rectangles and squares. It involves creating classes to represent these shapes, implementing various methods to manipulate their attributes, and ensuring proper validation and serialization of data.

## Technologies
- Python 3
- Object-Oriented Programming (OOP)
- Serialization/Deserialization
- JSON

## Requirements
### General
- All files must be written in Python 3.
- All files must end with a newline.
- The first line of all files must be `#!/usr/bin/python3`.
- A `README.md` file is mandatory at the root of the project directory.
- Code must adhere to PEP 8 style guide.
- All modules, classes, and functions must be documented with docstrings.
- All files must be executable.
- All classes must inherit from the `Base` class.
- Unit tests must cover all files, classes, and methods.

### Directory Structure
The directory structure should be organized as follows:
```
project_directory/
│
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── rectangle.py
│   ├── square.py
│   └── ...
│
└── tests/
    ├── test_models/
    │   ├── __init__.py
    │   ├── test_base.py
    │   ├── test_rectangle.py
    │   ├── test_square.py
    │   └── ...
    └── ...
```

### Tasks
| Task Number | File Name        | Description                                         |
|-------------|------------------|-----------------------------------------------------|
| 0           | models/base.py   | Implement the `Base` class.                         |
| 1           | models/rectangle.py | Implement the `Rectangle` class.                 |
| 2           | models/square.py | Implement the `Square` class.                     |
| 3           | models/rectangle.py | Implement validation for attributes in the `Rectangle` class. |
| 4           | models/rectangle.py | Implement the `area` method in the `Rectangle` class. |
| 5           | models/rectangle.py | Implement the `display` method in the `Rectangle` class. |
| 6           | models/rectangle.py | Override the `__str__` method in the `Rectangle` class. |
| 7           | models/rectangle.py | Enhance the `display` method in the `Rectangle` class. |
| 8           | models/rectangle.py | Implement the `update` method in the `Rectangle` class. |
| 9           | models/rectangle.py | Enhance the `update` method in the `Rectangle` class. |
| 10          | models/square.py | Implement the `Square` class.                     |
| 11          | models/square.py | Implement the `size` getter and setter in the `Square` class. |
| 12          | models/square.py | Implement the `update` method in the `Square` class. |
| 13          | models/base.py   | Implement the `to_json_string` static method in the `Base` class. |
| 14          | models/base.py   | Implement the `save_to_file` class method in the `Base` class. |
| 15          | models/base.py   | Implement the `from_json_string` static method in the `Base` class. |
| 16          | models/base.py   | Implement the `create` class method in the `Base` class. |
| 17          | models/rectangle.py | Implement the `to_dictionary` method in the `Rectangle` class. |
| 18          | models/square.py | Implement the `to_dictionary` method in the `Square` class. |
| 19          | models/base.py   | Implement the `from_json_string` static method in the `Base` class. |
| 20          | models/base.py   | Implement the `create` class method in the `Base` class. |
| 21          | models/rectangle.py | Implement the `to_dictionary` method in the `Rectangle` class. |

## Author :black_nib:
* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
