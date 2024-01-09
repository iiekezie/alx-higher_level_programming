### Project: 0x07-python-test_driven_development

#### Table of Contents
1. **Project Overview**
2. **Technologies**
3. **Requirements**
4. **Directory Structure**
5. **Author**


### Project Overview

This project focuses on test-driven development (TDD) in Python. It consists of various tasks, each involving the creation of functions and corresponding test cases. The tasks cover topics such as integers addition, matrix operations, string manipulation, and more. The goal is to reinforce the importance of writing tests before actual code implementation.

### Technologies

- Python 3.8.5
- Testing framework: `doctest` and `unittest`
- Code style checker: `pycodestyle`

### Requirements

#### Python Scripts
- Allowed editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Code should follow PEP8 guidelines (`pycodestyle` version 2.8.*)
- All files must be executable
- The length of files will be tested using `wc`

#### Python Test Cases
- All test files should end with a new line
- All test files should be inside a folder named `tests`
- All test files should have the extension `.txt`
- All tests should be executed by using the command: `python3 -m doctest ./tests/*`
- All modules and functions should have documentation
- Documentation should be meaningful sentences explaining the purpose
- Collaboration on test cases is encouraged

### Directory Structure

```plaintext
alx-higher_level_programming/
│
└── 0x07-python-test_driven_development/
    ├── 0-add_integer.py
    ├── 1-divide_matrix.py
    ├── 2-say_my_name.py
    ├── 3-print_square.py
    ├── 4-text_indentation.py
    ├── 5-max_integer.py
    ├── tests/
    │   ├── 0-add_integer.txt
    │   ├── 1-divide_matrix.txt
    │   ├── 2-say_my_name.txt
    │   ├── 3-print_square.txt
    │   ├── 4-text_indentation.txt
    │   ├── 5-max_integer_test.py
    │   ├── 6-matrix_mul.txt
    │   ├── 100-matrix_mul.txt
    │   ├── 101-lazy_matrix_mul.txt
    │   └── README.md (for test explanations)
    ├── README.md
    └── ...
```

### Tasks Table

| Task Number | File Name                       | Description                                              | Prototype                                          |
|-------------|---------------------------------|----------------------------------------------------------|----------------------------------------------------|
| 0           | 0-add_integer.py                | Integers addition                                        | `def add_integer(a, b=98):`                         |
| 1           | 1-divide_matrix.py               | Divide a matrix                                          | `def matrix_divided(matrix, div):`                  |
| 2           | 2-say_my_name.py                | Say my name                                              | `def say_my_name(first_name, last_name=""):`       |
| 3           | 3-print_square.py               | Print square                                             | `def print_square(size):`                          |
| 4           | 4-text_indentation.py           | Text indentation                                        | `def text_indentation(text):`                      |
| 5           | 5-max_integer.py                | Max integer - Unittest                                   | `def max_integer(list=[]):`                       |
| 6           | 6-matrix_mul.py                 | Matrix multiplication                                    | `def matrix_mul(m_a, m_b):`                        |
| 7           | 101-lazy_matrix_mul.py          | Lazy matrix multiplication (using NumPy)                 | `def lazy_matrix_mul(m_a, m_b):`                   |
| 8           | 102-python.c                    | CPython #3: Python Strings                               | `void print_python_string(PyObject *p);`         |


### Author :black_nib:

* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
