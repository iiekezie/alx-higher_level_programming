# Project Title: 0x0B. Python - Input/Output


## Project Overview
This project involves the implementation of various file input/output operations and JSON serialization in Python. The tasks cover a range of topics, from reading and writing files to working with JSON data. The project consists of several Python scripts, each addressing a specific task. Below is a brief summary of the tasks and the corresponding files

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [Task 0: Read file](#task-0-read-file)
  - [Task 1: Write to a file](#task-1-write-to-a-file)
  - [Task 2: Append to a file](#task-2-append-to-a-file)
  - [Task 3: To JSON string](#task-3-to-json-string)
  - [Task 4: From JSON string to Object](#task-4-from-json-string-to-object)
  - [Task 5: Save Object to a file](#task-5-save-object-to-a-file)
  - [Task 6: Create object from a JSON file](#task-6-create-object-from-a-json-file)
  - [Task 7: Load, add, save](#task-7-load-add-save)
  - [Task 8: Class to JSON](#task-8-class-to-json)
  - [Task 9: Student to JSON](#task-9-student-to-json)
  - [Task 10: Student to JSON with filter](#task-10-student-to-json-with-filter)
  - [Task 11: Student to disk and reload](#task-11-student-to-disk-and-reload)
  - [Task 12: Pascal's Triangle](#task-12-pascals-triangle)
  - [Task 13: Search and update](#task-13-search-and-update)
  - [Task 14: Log parsing](#task-14-log-parsing)
- [Author](#author)



## Technologies
Based on the provided code snippets, it appears that the project primarily involves Python and focuses on file input/output operations and JSON serialization. Here are the key technologies and concepts used in the project:

1. **Python:**
   - The entire project is implemented in Python, leveraging its simplicity and readability for handling file operations and working with JSON.

2. **File Input/Output:**
   - The project involves reading from and writing to text files. Python provides built-in functions and methods for efficient file I/O operations.

3. **JSON Serialization:**
   - The tasks related to converting objects to and from JSON format highlight the use of Python's `json` module. This module simplifies the serialization and deserialization of JSON data.

4. **Functions:**
   - The code is organized into functions, which encapsulate specific tasks. Functions promote modularity and reusability in the codebase.

5. **Exception Handling:**
   - Some code snippets include error handling mechanisms, such as using `try-except` blocks to catch potential exceptions during file operations.

6. **String Manipulation:**
   - String manipulation is utilized, particularly in tasks involving reading, writing, and manipulating text data.

## Requirements
	- Python Scripts
	- Allowed editors: vi, vim, emacs
	- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
	- All your files should end with a new line
	- The first line of all your files should be exactly #!/usr/bin/python3
	- A README.md file, at the root of the folder of the project, is mandatory
	- Your code should use the pycodestyle (version 2.8.*)
	- All your files must be executable
	- The length of your files will be tested using wc

## Tasks

| File Name                  | Description                                                                                                           | Prototype                                                  |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **0-read_file.py**          | Reads a text file (UTF8) and prints it to stdout.                                                                    | `def read_file(filename=""):`                              |
| **1-write_file.py**         | Writes a string to a text file (UTF8) and returns the number of characters written.                                  | `def write_file(filename="", text=""):`                    |
| **2-append_write.py**       | Appends a string at the end of a text file (UTF8) and returns the number of characters added.                       | `def append_write(filename="", text=""):`                  |
| **3-to_json_string.py**     | Returns the JSON representation of an object (string).                                                               | `def to_json_string(my_obj):`                               |
| **4-from_json_string.py**   | Returns an object (Python data structure) represented by a JSON string.                                              | `def from_json_string(my_str):`                             |
| **5-save_to_json_file.py**  | Writes an Object to a text file, using a JSON representation.                                                        | `def save_to_json_file(my_obj, filename):`                 |
| **6-load_from_json_file.py**| Creates an Object from a “JSON file”.                                                                                 | `def load_from_json_file(filename):`                        |
| **7-add_item.py**           | Adds all arguments to a Python list and saves them to a file in JSON representation.                                  | Script, no function prototype.                             |
| **8-class_to_json.py**      | Returns the dictionary description for JSON serialization of an object.                                              | `def class_to_json(obj):`                                   |
| **9-student.py**            | Defines a student class with attributes and a method to retrieve a dictionary representation.                        | Class, no function prototype.                              |
| **10-student.py**           | Extends the student class to allow filtering attributes for JSON serialization.                                      | Class, no function prototype.                              |
| **11-student.py**           | Extends the student class to include methods for saving and reloading from JSON.                                      | Class, no function prototype.                              |
| **12-pascal_triangle.py**   | Generates Pascal's Triangle up to a given level.                                                                     | `def pascal_triangle(n):`                                  |
| **100-append_after.py**     | Inserts a line of text to a file after each line containing a specific string.                                        | `def append_after(filename="", search_string="", new_string=""):` |
| **101-parser.py**           | Reads stdin line by line and computes metrics based on log entries.                                                  | Script, no function prototype.   


## Author :black_nib:

* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
