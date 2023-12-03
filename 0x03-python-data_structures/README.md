# Project: 0x03. Python - Data Structures: Lists, Tuples

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies](#technologies)
3. [Requirements](#requirements)
   - [General](#general)
   - [Directory Structure](#directory-structure)
   - [Tasks](#tasks)
   - [C Scripts](#c-scripts)
4. [Author](#author)

---

### Project Overview

Project done during **Full Stack Software Engineering studies** at **ALX Software Engineering **. The project focuses on Python programming and data structures, specifically lists and tuples. The tasks aim to reinforce understanding of various concepts, such as list manipulation, tuple operations, and general Python programming skills.

### Technologies

- Python 3.8.5
- C
- Ubuntu 20.04 LTS

### Requirements

#### General

- Allowed editors: vi, vim, emacs
- All Python files interpreted on Ubuntu 20.04 LTS using Python3 (version 3.8.5)
- All C files compiled on Ubuntu 20.04 LTS using Python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/python3` for Python scripts
- README.md file at the root of the project folder is mandatory
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- Length of files will be tested using wc

#### Directory Structure

The directory structure for the project is as follows:

```
project-root/
│
├── C_scripts/
│   ├── lists.h
│   ├── 1-element_at.c
│   ├── 2-replace_in_list.c
│   ├── ...
│   └── 13-is_palindrome.c
│
├── Python_scripts/
│   ├── 0-print_list_integer.py
│   ├── 1-element_at.py
│   ├── 2-replace_in_list.py
│   ├── ...
│   └── 10-divisible_by_2.py
│
├── 12-switch.py
├── 13-is_palindrome.c
├── 100-print_python_list_info.c
└── README.md
```

#### Tasks

| Task Number | File Name                             | Description                                           | Prototype                                      |
|-------------|---------------------------------------|-------------------------------------------------------|------------------------------------------------|
| 0           | 0-print_list_integer.py               | Print a list of integers                              | `def print_list_integer(my_list=[]):`            |
| 1           | 1-element_at.py                       | Secure access to an element in a list                 | `def element_at(my_list, idx):`                  |
| 2           | 2-replace_in_list.py                  | Replace element in a list                             | `def replace_in_list(my_list, idx, element):`    |
| 3           | 3-print_reversed_list_integer.py      | Print a list of integers in reverse order            | `def print_reversed_list_integer(my_list=[]):`  |
| 4           | 4-new_in_list.py                      | Replace in a copy                                      | `def new_in_list(my_list, idx, element):`        |
| 5           | 5-no_c.py                             | Remove all characters c and C from a string          | `def no_c(my_string):`                           |
| 6           | 6-print_matrix_integer.py             | Lists of lists = Matrix                                | `def print_matrix_integer(matrix=[[]]):`        |
| 7           | 7-add_tuple.py                        | Tuples addition                                        | `def add_tuple(tuple_a=(), tuple_b=()):`       |
| 8           | 8-multiple_returns.py                 | More returns                                           | `def multiple_returns(sentence):`               |
| 9           | 9-max_integer.py                      | Find the max                                           | `def max_integer(my_list=[]):`                  |
| 10          | 10-divisible_by_2.py                  | Only by 2                                             | `def divisible_by_2(my_list=[]):`               |
| 11          | 11-delete_at.py                       | Delete at                                             | `def delete_at(my_list=[], idx=0):`            |
| 12          | 12-switch.py                          | Switch                                                | (Code insertion required in the provided file) |
| 13          | 13-is_palindrome.c                    | Linked list palindrome                                | `int is_palindrome(listint_t **head);`          |
| 14          | 100-print_python_list_info.c          | CPython #0: Python lists                               | `void print_python_list_info(PyObject *p);`   |

#### C Scripts

- All C scripts should follow the specified requirements mentioned in the tasks.

## Author :black_nib:

* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
