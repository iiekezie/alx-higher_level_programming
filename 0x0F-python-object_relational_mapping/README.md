## Python Object-Relational Mapping Project
This project explores the connection between Python and MySQL databases using Object-Relational Mapping (ORM). 

### Project Overview
The project consists of ten tasks, progressively introducing you to working with MySQL databases through Python scripts. You'll start by using the `MySQLdb` module to execute basic queries and then transition to using SQLAlchemy, a popular ORM library.

### Technologies
* Python (version 3.8.5)
* MySQL (version 8.0 recommended)
* MySQLdb (version 2.0.x)
* SQLAlchemy (version 1.4.x)

### Requirements
* **Operating System:** Ubuntu 20.04 LTS
* **Text Editor:**  vi, vim, or emacs
* **Python Virtual Environment:** Recommended for managing project dependencies

**Here's how to set up your environment:**

1. **Install Python 3.8 and virtualenv:**

   ```bash
   sudo apt-get install python3.8-venv
   source venv/bin/activate
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install MySQL and MySQLdb:**

   ```bash
   sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
   sudo pip3 install mysqlclient
   ```

4. **Install SQLAlchemy:**

   ```bash
   sudo pip3 install SQLAlchemy
   ```

**Additional Notes:**

* Ensure your MySQL server is running on `localhost` at port `3306`.
* You can ignore the warning message about `@SESSION.GTID_EXECUTED` during installation.

### Table of Contents

1. Project Overview
2. Technologies
3. Requirements
4. General Requirements
5. Tasks
    * 0. Get all states
    * 1. Filter states
    * 2. Filter states by user input
    * 3. SQL Injection Safe Filter
    * 4. Cities by states
    * 5. All cities by state
    * 6. First state model
    * 7. All states via SQLAlchemy
    * 8. First state
    * 9. Contains 'a'
    * 10. Get a state
    * 12. Add a new state
    * 13. Delete states
    * 14. Cities in state
    * 15. City relationship
    * 16. List relationship
    * 17. From city

6. Prototype (Optional)

### General Requirements

* All code files should start with `#!/usr/bin/python3`
* All files should end with a newline character
* Use `pycodestyle` for code style checking
* All files must be executable
* Document your code using docstrings (functions, classes, modules)

### Tasks

Each task comes with a detailed description, expected output format, and a reference to the relevant code file.

**Please refer to the individual task descriptions for specific instructions.**

### Prototype (Optional)

You can optionally include a prototype or visual representation of your project's functionality here. This could be a flowchart, UML diagram, or a basic wireframe.

### Author
**Ifeanyi I Ekezie**

* [GitHub](https://github.com/iiekezie)