# Project:  0x0A. Python - Inheritance

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies](#technologies)
3. [Requirements](#requirements)
4. [Directory Structure](#directory-structure)
5. [Tasks](#tasks)
    - [Task 0: Lookup](#task-0-lookup)
    - [Task 1: My List](#task-1-my-list)
    - [Task 2: Exact Same Object](#task-2-exact-same-object)
    - [Task 3: Same Class or Inherit From](#task-3-same-class-or-inherit-from)
    - [Task 4: Only Subclass Of](#task-4-only-subclass-of)
    - [Task 5: Geometry Module](#task-5-geometry-module)
    - [Task 6: Improve Geometry](#task-6-improve-geometry)
    - [Task 7: Integer Validator](#task-7-integer-validator)
    - [Task 8: Rectangle](#task-8-rectangle)
    - [Task 9: Full Rectangle](#task-9-full-rectangle)
    - [Task 10: Square #1](#task-10-square-1)
    - [Task 11: Square #2](#task-11-square-2)
    - [Task 12: My Integer](#task-12-my-integer)
    - [Task 13: Can I?](#task-13-can-i)
6. [Author](#author)


## Project Overview
This project is part of the ALX Higher Level Programming curriculum and focuses on Python programming concepts related to inheritance. The primary goals of this project are to reinforce understanding of:

- Why Python programming is awesome
- Concepts of superclass, base class, or parent class
- Subclass and how to list all attributes and methods of a class or instance
- Inheriting a class from another
- Defining a class with multiple base classes
- Overriding a method or attribute inherited from the base class
- Default class every class inherits from
- Purpose and usage of inheritance
- Functions like `isinstance`, `issubclass`, `type`, and `super` built-in functions

## Technologies
- Python
- Object-Oriented Programming (OOP)
- Inheritance

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Code should use the pycodestyle (version 2.8.*)
- All files must be executable
- The length of files will be tested using wc

## Directory Structure
Description of the organization of project files and folders.
## Directory Structure
```
0x0A-python-inheritance/
│-- 0-lookup.py
│-- 1-my_list.py
│-- 2-is_same_class.py
│-- 3-is_kind_of_class.py
│-- 4-inherits_from.py
│-- 5-base_geometry.py
│-- 6-base_geometry.py
│-- 7-base_geometry.py
│-- 8-rectangle.py
│-- 9-rectangle.py
│-- 10-square.py
│-- 11-square.py
│-- 100-my_int.py
│-- 101-add_attribute.py
│-- tests/
│   │-- 1-my_list.txt
│   │-- 7-base_geometry.txt
│   │-- ...
│-- README.md
```


## Tasks

| Task Number | File Name | Description | Prototype | Testing |
|-------------|-----------|-------------|-----------|---------|
| 0 | 0-lookup.py | Write a function that returns the list of available attributes and methods of an object. | `def lookup(obj):` | [Test](#task-0-lookup) |
| 1 | 1-my_list.py | Write a class MyList that inherits from list and has a public instance method `def print_sorted(self)` that prints the list, but sorted (ascending sort). | | [Test](#task-1-my-list) |
| 2 | 2-is_same_class.py | Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False. | `def is_same_class(obj, a_class):` | [Test](#task-2-exact-same-object) |
| 3 | 3-is_kind_of_class.py | Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False. | `def is_kind_of_class(obj, a_class):` | [Test](#task-3-same-class-or-inherit-from) |
| 4 | 4-inherits_from.py | Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False. | `def inherits_from(obj, a_class):` | [Test](#task-4-only-subclass-of) |
| 5 | 5-base_geometry.py | Write an empty class BaseGeometry. | | [Test](#task-5-geometry-module) |
| 6 | 6-base_geometry.py | Write a class BaseGeometry (based on 5-base_geometry.py) with a public instance method `def area(self):` that raises an Exception with the message area() is not implemented. | | [Test](#task-6-improve-geometry) |
| 7 | 7-base_geometry.py | Write a class BaseGeometry (based on 6-base_geometry.py) with public instance methods `def area(self):` and `def integer_validator(self, name, value):` | | [Test](#task-7-integer-validator) |
| 8 | 8-rectangle.py | Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). | | [Test](#task-8-rectangle) |
| 9 | 9-rectangle.py | Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py) | | [Test](#task-9-full-rectangle) |
| 10 | 10-square.py | Write a class Square that inherits from Rectangle (9-rectangle.py). | | [Test](#task-10-square-1) |
| 11 | 11-square.py | Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py) | | [Test](#task-11-square-2) |
| 12 | 12-my_int.py | Write a class MyInt that inherits from int. | | [Test](#task-12-my-integer) |
| 13 | 13-can_i.py | Write a function that adds a new attribute to an object if it’s possible. | `def add_attribute(obj, name, value):` | [Test](#task-13-can-i) |

## Author :black_nib:

* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
