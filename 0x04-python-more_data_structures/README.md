# Project Name: # 0x04. Python - More Data Structures: Set, Dictionary

![Python logo]
This project is part of the ALX Higher Level Programming curriculum. It covers the topics of sets, dictionaries, and more data structures in Python.

## Project Overview
This project consists of Python scripts that cover various topics related to more advanced data structures in Python. The tasks include working with lists, dictionaries, sets, and more. Each script addresses a specific task and provides a solution in Python.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies](#technologies)
3. [Requirements](#requirements)
    - [General](#general)
4. [Directory Structure](#directory-structure)
5. [Tasks](#tasks)
    - [Task 0](#0)
    - [Task 1](#1)
    - [Task 2](#2)
    - [Task 3](#3)
    - [Task 4](#4)
    - [Task 5](#5)
    - [Task 6](#6)
    - [Task 7](#7)
    - [Task 8](#8)
    - [Task 9](#9)
    - [Task 10](#10)
    - [Task 11](#11)
    - [Task 12](#12)
    - [Task 100](#100)
    - [Task 101](#101)
    - [Task 102](#102)
    - [Task 103](#103)
6. [C Scripts](#c-scripts)
    - [Script 1](#script-1)
    - [Script 2](#script-2)
7. [Image Structures](#image-structures)
    - [Structure 1](#structure-1)
    - [Structure 2](#structure-2)
8. [Author](#author)


## Technologies

- Python 3.8.5
- pycodestyle 2.8.*

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

## Directory Structure
The project directory structure is as follows:

```
alx-higher_level_programming/
│
└── 0x04-python-more_data_structures/
    ├── 0-square_matrix_simple.py
    ├── 1-search_replace.py
    ├── 2-uniq_add.py
    ├── 3-common_elements.py
    ├── 4-only_diff_elements.py
    ├── 5-number_keys.py
    ├── 6-print_sorted_dictionary.py
    ├── 7-update_dictionary.py
    ├── 8-simple_delete.py
    ├── 9-multiply_by_2.py
    ├── 10-best_score.py
    ├── 11-multiply_list_map.py
    ├── 12-roman_to_int.py
    ├── 100-weight_average.py
    ├── 101-square_matrix_map.py
    ├── 102-complex_delete.py
    ├── 103-python.c
    ├── 103-tests.py
    └── README.md
```

### Tasks
| Task Number | File Name                    | Description                                            | Prototype                                                     |
|-------------|-----------------------------|--------------------------------------------------------|---------------------------------------------------------------|
| 0           | 0-square_matrix_simple.py   | Computes the square value of all integers in a matrix. | `def square_matrix_simple(matrix=[]):`                          |
| 1           | 1-search_replace.py          | Replaces all occurrences of an element in a list.      | `def search_replace(my_list, search, replace):`                |
| 2           | 2-uniq_add.py                | Adds all unique integers in a list.                     | `def uniq_add(my_list=[]):`                                    |
| 3           | 3-common_elements.py         | Returns a set of common elements in two sets.           | `def common_elements(set_1, set_2):`                           |
| 4           | 4-only_diff_elements.py      | Returns a set of elements present in only one set.      | `def only_diff_elements(set_1, set_2):`                        |
| 5           | 5-number_keys.py             | Returns the number of keys in a dictionary.             | `def number_keys(a_dictionary):`                               |
| 6           | 6-print_sorted_dictionary.py | Prints a dictionary by ordered keys.                    | `def print_sorted_dictionary(a_dictionary):`                  |
| 7           | 7-update_dictionary.py       | Replaces or adds key/value in a dictionary.             | `def update_dictionary(a_dictionary, key, value):`            |
| 8           | 8-simple_delete.py           | Deletes a key in a dictionary.                          | `def simple_delete(a_dictionary, key=""):`                     |
| 9           | 9-multiply_by_2.py          | Returns a new dictionary with all values multiplied by 2 | `def multiply_by_2(a_dictionary):`                             |
| 10          | 10-best_score.py             | Returns a key with the biggest integer value.           | `def best_score(a_dictionary):`                                |
| 11          | 11-multiply_list_map.py      | Multiplies all values in a list by a number using map.  | `def multiply_list_map(my_list=[], number=0):`                |
| 12          | 12-roman_to_int.py           | Converts a Roman numeral to an integer.                 | `def roman_to_int(roman_string):`                              |
| 100         | 100-weight_average.py        | Returns the weighted average of integers tuple.         | `def weight_average(my_list=[]):`                             |
| 101         | 101-square_matrix_map.py     | Computes the square value of all integers in a matrix using map | `def square_matrix_map(matrix=[]):`                           |
| 102         | 102-complex_delete.py        | Deletes keys with a specific value in a dictionary.     | `def complex_delete(a_dictionary, value):`                    |
| 103         | 103-python.c                 | C functions to print basic info about Python lists and bytes objects | `void print_python_list(PyObject *p);`<br>`void print_python_bytes(PyObject *p);` |

## C Scripts

### Script 1

A C script that performs a specific task.

```c
// C script 1
#include <stdio.h>

void script1_function() {
    // Implementation of the script
    printf("This is C script 1\n");
}
```

### Script 2

Another C script for a different task.

```c
// C script 2
#include <stdio.h>

void script2_function() {
    // Implementation of the script
    printf("This is C script 2\n");
}
```

## Image Structures

### Structure 1

Description of the first image structure.

![Image Structure 1](images/structure1.png)

### Structure 2

Description of the second image structure.

![Image Structure 2](images/structure2.png)

Some tasks may require writing C scripts to test the Python functions. These scripts should be placed in a subfolder called `tests` and have the extension `.c`. For example, the C script for task 0 should be named `tests/0-square_matrix_simple.c`.

## Author :black_nib:
**Ifeanyi I Ekezie**
- GitHub: [iiekezie](:wq
https://github.com/iiekezie)
