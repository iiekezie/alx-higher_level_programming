# Project: N-Queens Solver  0x08. Python - More Classes and Objects

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies](#technologies)
3. [Requirements](#requirements)
    - [General](#general)
    - [Directory Structure](#directory-structure)
4. [Tasks](#tasks)
4. [Author](#authors)

## Project Overview
This project involves solving the N-Queens puzzle, a classic chess problem where N queens need to be placed on an N×N chessboard without attacking each other.

## Technologies
- Python
- Golang (as per user's profile)

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Code should use pycodestyle (version 2.8.*)
- All files must be executable

### Directory Structure
The directory structure of the project should follow the standard conventions.

```
├── 0x08-python-more_classes
│ ├── 0-rectangle.py
│ ├── 1-rectangle.py
│ ├── 2-rectangle.py
│ ├── 3-rectangle.py
│ ├── 4-rectangle.py
│ ├── 5-rectangle.py
│ ├── 6-rectangle.py
│ ├── 7-rectangle.py
│ ├── 8-rectangle.py
│ ├── 9-rectangle.py
│ └── 101-nqueens.py
├── README.md
└── 9-main.py
```

## Tasks

| Task Number | Task Description | Prototype |
|-------------|-------------------|-----------|
| Task 0      | Write an empty class Rectangle that defines a rectangle. | `class Rectangle: pass` |
| Task 1      | Define a class Rectangle that includes private instance attributes width and height, along with properties for retrieval and setting. | `class Rectangle: pass` |
| Task 2      | Extend the Rectangle class with methods for calculating area and perimeter. | `def area(self): pass`<br>`def perimeter(self): pass` |
| Task 3      | Enhance the Rectangle class to include string representation using `print()` and `str()`. | `def __str__(self): pass` |
| Task 4      | Implement a method to allow the recreation of a new instance by using `eval()`. | `def __repr__(self): pass` |
| Task 5      | Print a message when an instance of Rectangle is deleted. | `def __del__(self): pass` |
| Task 6      | Implement a class attribute to keep track of the number of instances. | `number_of_instances = 0` |
| Task 7      | Add a class attribute `print_symbol` and adjust the representation of the rectangle accordingly. | `print_symbol = "#"`,<br> `def __str__(self): pass` |
| Task 8      | Implement a static method to compare rectangles based on their area. | `@staticmethod`<br>`def bigger_or_equal(rect_1, rect_2): pass` |
| Task 9      | Add a class method to create a new Rectangle instance with equal width and height. | `@classmethod`<br>`def square(cls, size=0): pass` |
| Task 10     | Solve the N-Queens puzzle for a given N, printing every possible solution. | `def solve_nqueens(N): pass` |


## Author :black_nib:

* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
