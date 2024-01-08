## Project: 0x06. Python - Classes and Objects

## Project Overview
This project involves the implementation of a Python class named "Square" and a linked list class named "SinglyLinkedList". The Square class represents a square, and the SinglyLinkedList class represents a singly linked list. The goal is to implement various functionalities related to squares and linked lists.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies](#technologies)
3. [Requirements](#requirements)
    - [General](#general)
4. [Data Structures](#data-structures)
5. [Tasks](#tasks)
    - [Task 0: My First Square](#task-0-my-first-square)
    - [Task 1: Square with Size](#task-1-square-with-size)
    - [Task 2: Size Validation](#task-2-size-validation)
    - [Task 3: Area of a Square](#task-3-area-of-a-square)
    - [Task 4: Access and Update Private Attribute](#task-4-access-and-update-private-attribute)
    - [Task 5: Printing a Square](#task-5-printing-a-square)
    - [Task 6: Coordinates of a Square](#task-6-coordinates-of-a-square)
    - [Task 7: Singly Linked List](#task-7-singly-linked-list)
    - [Task 8: Print Square Instance](#task-8-print-square-instance)
    - [Task 9: Compare 2 Squares](#task-9-compare-2-squares)
    - [Task 10: ByteCode -> Python #5](#task-10-bytecode--python-5)
6. [Author](#author)


## Technologies
- Python 3.8.5
- pycodestyle 2.8.* (for code style)

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- The length of files will be tested using wc
- All modules, classes, and functions must have documentation (docstrings)

## Data Structures
### Singly Linked List

````
A Singly Linked List is a fundamental data structure in computer science that consists of a sequence of elements, where each element points to the next one in the sequence. Unlike arrays, linked lists do not have a fixed size, and elements can be easily inserted or removed without the need to reallocate memory.

#### Node

The basic building block of a Singly Linked List is a Node. Each node in the list contains two components:
- **Data:** The actual data or value stored in the node.
- **Next:** A reference or link to the next node in the sequence.

Here's a simple representation of a Node class:

```python
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
```


## Tasks
| Task Number | File Name                     | Description                                        | Prototype                                      |
|-------------|-------------------------------|----------------------------------------------------|------------------------------------------------|
| 0           | [0-square.py](./0-square.py) | Define an empty class `Square`.                     | `class Square:`                                |
| 1           | [1-square.py](./1-square.py) | Square class with a private instance attribute `size`. Handle invalid size values. | `class Square:`<br/>`def __init__(self, size=0):` |
| 2           | [2-square.py](./2-square.py) | Add size validation to the Square class. Handle invalid size values. | `class Square:`<br/>`def __init__(self, size=0):` |
| 3           | [3-square.py](./3-square.py) | Add a public instance method `area` to calculate and return the square's area. | `class Square:`<br/>`def __init__(self, size=0):`<br/>`def area(self):` |
| 4           | [4-square.py](./4-square.py) | Add a property `size` to get and set the size attribute. Handle invalid size values. | `class Square:`<br/>`def __init__(self, size=0):`<br/>`@property`<br/>`def size(self):`<br/>`@size.setter`<br/>`def size(self, value):` |
| 5           | [5-square.py](./5-square.py) | Add a public instance method `my_print` to print the square with the character '#'. Handle size equal to 0. | `class Square:`<br/>`def __init__(self, size=0):`<br/>`def my_print(self):` |
| 6           | [6-square.py](./6-square.py) | Add a private instance attribute `position` to the Square class. Add properties to get and set the position attribute. Update the `my_print` method to use the position. Handle invalid position values. | `class Square:`<br/>`def __init__(self, size=0, position=(0, 0)): `<br/>`@property`<br/>`def position(self):`<br/>`@position.setter`<br/>`def position(self, value):`<br/>`def my_print(self):` |
| 7           | [100-singly_linked_list.py](./100-singly_linked_list.py) | Implement a class `Node` representing a node of a singly linked list.

 Implement a class `SinglyLinkedList` representing a singly linked list with a sorted insert method. | `class Node:`<br/>`def __init__(self, data, next_node=None):`<br/><br/>`class SinglyLinkedList:`<br/>`def __init__(self):`<br/>`def sorted_insert(self, value):` |
| 8           | [101-square.py](./101-square.py) | Enhance the Square class to have a `__str__` method for string representation. | `class Square:`<br/>`def __init__(self, size=0):`<br/>`def __str__(self):` |
| 9           | [102-square.py](./102-square.py) | Enhance the Square class with methods `__eq__` and `__ne__` for comparing squares based on their size. | `class Square:`<br/>`def __init__(self, size=0):`<br/>`def __eq__(self, other):`<br/>`def __ne__(self, other):` |
| 10          | [103-magic_class.py](./103-magic_class.py) | Write a Python class `MagicClass` that mimics the provided bytecode. | `import math`<br/><br/>`class MagicClass:`<br/>`def __init__(self, radius=0):`<br/>`def area(self):`<br/>`def circumference(self):` |

## Author :black_nib:

* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
