# Project: 0x02. Python - import & modules

## Table of Contents

1. [Project Overview](#project-overview)
2. [Learning Objectives](#learning-objectives)
3. [Directory Structure](#directory-structure)
4. [Requirements](#requirements)
5. [Tasks](#tasks)
    - [Task 0](#task-0)
    - [Task 1](#task-1)
    - [Task 2](#task-2)
    - [Task 3](#task-3)
    - [Task 4](#task-4)
    - [Task 5](#task-5)
    - [Task 100](#task-100)
    - [Task 101](#task-101)
    - [Task 102](#task-102)
    - [Task 103](#task-103)
6. [Python Scripts](#python-scripts)
7. [C Scripts](#c-scripts)
8. [Additional Notes](#additional-notes)
8. [Author](#Author)

## Description
Project done during **Full Stack Software Engineering studies** at **ALX Software Engineering **. It aims to learn how to import functions, how to create modules and how to use command line arguments in **Python**. This project focuses on Python programming, specifically the use of import statements and modules. The tasks involve creating Python scripts to import functions from other files, handling command line arguments, and understanding module creation. The project also covers some advanced topics such as bytecode, avoiding system calls, and creating concise programs.

## Technologies
* Shell Scripts are written in Bash 4.3.11(1)
* Python Scripts are written with Python 3.4.3
* C files are compiled using `gcc 4.8.4`
* Tested on Ubuntu 14.04 LTS

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

## Directory Structure

```
0x02-python-import_modules/
│
├── 0-add.py
├── 1-calculation.py
├── 2-args.py
├── 3-infinite_add.py
├── 4-hidden_discovery.py
├── 5-variable_load.py
├── 100-my_calculator.py
├── 101-easy_print.py
├── 102-magic_calculation.py
├── 103-fast_alphabet.py
├── README.md
│
├── python_scripts/
│   ├── add_0.py
│   ├── calculator_1.py
│   ├── variable_load_5.py
│   ├── magic_calculation_102.py
│   └── hidden_4.pyc
│
└── c_scripts/
    └── hidden_4.c
```

## Tasks

| Task Number | File Name | Description | Prototype |
|-------------|-----------|-------------|-----------|
| 0 | 0-add.py | Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3` | N/A |
| 1 | 1-calculation.py | Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result. | N/A |
| 2 | 2-args.py | Write a program that prints the number of and the list of its arguments. | N/A |
| 3 | 3-infinite_add.py | Write a program that prints the result of the addition of all arguments. | N/A |
| 4 | 4-hidden_discovery.py | Write a program that prints all the names defined by the compiled module `hidden_4.pyc`. | N/A |
| 5 | 5-variable_load.py | Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value. | N/A |
| 100 | 100-my_calculator.py | Write a program that imports all functions from the file `calculator_1.py` and handles basic operations. | Usage: `./100-my_calculator.py a operator b` |
| 101 | 101-easy_print.py | Write a program that prints `#pythoniscool`, followed by a new line, in the standard output. | N/A |
| 102 | 102-magic_calculation.py | Write the Python function `def magic_calculation(a, b):` that does exactly the same as the provided Python bytecode. | N/A |
| 103 | 103-fast_alphabet.py | Write a program that prints the alphabet in uppercase, followed by a new line. | N/A |

### C Scripts
- **Allowed Editors:** vi, vim, emacs
- **

*Note: Replace N/A in the Prototype column with the actual prototype of the Python functions.*


## Author :black_nib:

* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
