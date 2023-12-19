# Project; 0x05. Python - Exceptions

## Project Overview
This project focuses on Python programming concepts related to exceptions and error handling. It includes a set of tasks that cover various aspects of handling exceptions in Python, from printing elements of a list safely to implementing functions with exception handling.

## Technologies
- Python 3.8.5
- Ubuntu 20.04 LTS
- pycodestyle 2.8.*

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- The length of files will be tested using `wc`

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Provided by ALX Software Engineering.

### Tasks
- Task-specific requirements are documented within each task description

## Directory Structure
```
.
├── 0x05-python-exceptions
│   ├── 0-safe_print_list.py
│   ├── 1-safe_print_integer.py
│   ├── 2-safe_print_list_integers.py
│   ├── 3-safe_print_division.py
│   ├── 4-list_division.py
│   ├── 5-raise_exception.py
│   ├── 6-raise_exception_msg.py
│   ├── 100-safe_print_integer_err.py
│   ├── 101-safe_function.py
│   ├── 102-magic_calculation.py
│   └── 103-python.c
├── .gitignore
└── README.md
```

### Tasks with Example

1. **Safe List Printing**

   - File Name: `0-safe_print_list.py`
   - Description: Write a function that prints a specified number of elements from a list.
   - Prototype: `def safe_print_list(my_list=[], x=0):`
   - Additional Requirements:
     - Use `try`/`except`.
     - Do not use `import` or `len()`.

   ```python
   # Example Usage
   my_list = [1, 2, 3, 4, 5]
   nb_print = safe_print_list(my_list, 2)
   ```

2. **Safe Printing of Integers**

   - File Name: `1-safe_print_integer.py`
   - Description: Write a function that prints an integer using "{:d}".format().
   - Prototype: `def safe_print_integer(value):`
   - Additional Requirements:
     - Use `try`/`except`.
     - Do not use `import` or `type()`.

   ```python
   # Example Usage
   value = 89
   has_been_print = safe_print_integer(value)
   ```

3. **Print and Count Integers**

   - File Name: `2-safe_print_list_integers.py`
   - Description: Write a function that prints the first x elements of a list, only printing integers.
   - Prototype: `def safe_print_list_integers(my_list=[], x=0):`
   - Additional Requirements:
     - Use `try`/`except`.
     - Do not use `import` or `len()`.

   ```python
   # Example Usage
   my_list = [1, 2, 3, 4, 5]
   nb_print = safe_print_list_integers(my_list, 2)
   ```

4. **Integers Division with Debug**

   - File Name: `3-safe_print_division.py`
   - Description: Write a function that divides two integers and prints the result.
   - Prototype: `def safe_print_division(a, b):`
   - Additional Requirements:
     - Use `try`/`except`/`finally`.
     - Use "{}".format() to print the result.
     - Do not use `import`.

   ```python
   # Example Usage
   a = 12
   b = 2
   result = safe_print_division(a, b)
   ```

5. **Divide a List**

   - File Name: `4-list_division.py`
   - Description: Write a function that divides element by element two lists.
   - Prototype: `def list_division(my_list_1, my_list_2, list_length):`
   - Additional Requirements:
     - Use `try`/`except`/`finally`.
     - Do not use `import`.

   ```python
   # Example Usage
   my_l_1 = [10, 8, 4]
   my_l_2 = [2, 4, 4]
   result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
   ```

6. **Raise Exception**

   - File Name: `5-raise_exception.py`
   - Description: Write a function that raises a type exception.
   - Prototype: `def raise_exception():`
   - Additional Requirements:
     - Do not use `import`.

   ```python
   # Example Usage
   try:
       raise_exception()
   except TypeError as te:
       print("Exception raised")
   ```

7. **Raise a Message**

   - File Name: `6-raise_exception_msg.py`
   - Description: Write a function that raises a name exception with a message.
   - Prototype: `def raise_exception_msg(message=""):`
   - Additional Requirements:
     - Do not use `import`.

   ```python
   # Example Usage
   try:
       raise_exception_msg("C is fun")
   except NameError as ne:
       print(ne)
   ```

8. **Safe Integer Print with Error Message**

   - File Name: `100-safe_print_integer_err.py`
   - Description: Write a function that prints an integer.
   - Prototype: `def safe_print_integer_err(value):`
   - Additional Requirements:
     - Use `try`/`except`.
     - Use "{}".format() to print as an integer.
     - Do not use `type()`.

   ```python
   # Example Usage
   value = 89
   has_been_print = safe_print_integer_err(value)
   ```

9. **Safe Function**

   - File Name: `101-safe_function.py`
   - Description: Write a function that executes a function safely.
   - Prototype: `def safe_function(fct, *args):`
   - Additional Requirements:
     - Use `try`/`except`.

   ```python
   # Example Usage
   def my_div(a, b):
       return a / b

   result = safe_function(my_div, 10, 2)
   ```

10. **ByteCode -> Python #4**

    - File Name: `102-magic_calculation.py`
    - Description: Write a Python function that does the same as the provided Python bytecode.

   ```python
   # Example Usage
   def magic_calculation(a, b):
       # Your implementation
   ```

11. **CPython #2: PyFloatObject**

    - File Name: `103-python.c`
    - Description: Create three C functions that print basic info about Python lists, Python bytes, and Python float objects.

   ```python
   # Example Usage
   import ctypes
   lib = ctypes.CDLL('./libPython.so')
   lib.print_python_list.argtypes = [ctypes.py_object]
   lib.print_python_bytes.argtypes = [ctypes.py_object]
   lib.print_python_float.argtypes = [ctypes.py_object]
   s = b"Hello"
   lib.print_python_bytes(s)
   ```

## Tasks

| Task Number | File Name                     | Description                                                   | Prototype                                                   |
|-------------|-------------------------------|---------------------------------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------|
| 0           | 0-safe_print_list.py          | Print elements of a list safely                                | `def safe_print_list(my_list=[], x=0):`                     |
| 1           | 1-safe_print_integer.py       | Print an integer with "{:d}".format()                         | `def safe_print_integer(value):`                            |
| 2           | 2-safe_print_list_integers.py | Print and count integers in a list                             | `def safe_print_list_integers(my_list=[], x=0):`           |
| 3           | 3-safe_print_division.py      | Divide 2 integers and print the result                         | `def safe_print_division(a, b):`                            | 
| 4           | 4-list_division.py            | Divide element by element in two lists                         | `def list_division(my_list_1, my_list_2, list_length):`    |
| 5           | 5-raise_exception.py          | Raise a type exception                                         | `def raise_exception():`                                    |
| 6           | 6-raise_exception_msg.py      | Raise a name exception with a message                          | `def raise_exception_msg(message=""):`                     | 
| 7           | 100-safe_print_integer_err.py | Safe integer print with error message                          | `def safe_print_integer_err(value):`                       |
| 8           | 101-safe_function.py          | Execute a function safely                                      | `def safe_function(fct, *args):`                            |
| 9           | 102-magic_calculation.py       | Replicate Python bytecode                                      | `def magic_calculation(a, b):`                              |
| 10          | 103-python.c                  | C functions for Python lists, bytes, and float objects        | See task description for prototypes and details             |

## Author 🖋️
- **Ifeanyi I Ekezie** - [iiekezie](https://github.com/iiekezie)
