n - Network #0

## Project Overview
This project covers the basics of network programming using Bash and Python. It includes tasks on making HTTP requests using `curl`, handling HTTP headers, and working with JSON data. The project also includes a technical interview preparation task involving algorithmic problem-solving.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies](#technologies)
3. [Requirements](#requirements)
4. [Directory Structure](#directory-structure)
5. [Tasks](#tasks)
6. [C Scripts](#c-scripts)
7. [Author](#author)


## Technologies
- Bash
- Python 3.8.5
- `curl`

## Requirements
- All scripts are tested on Ubuntu 20.04 LTS
- All Bash scripts should be exactly 3 lines long
- All files should end with a new line and must be executable
- All Python files should adhere to `pycodestyle` (version 2.8.*)
- Documentation is required for all modules, classes, and functions

## Directory Structure
```
0x10-python-network_0
│
├── 0-body_size.sh
├── 1-body.sh
├── 2-delete.sh
├── 3-methods.sh
├── 4-header.sh
├── 5-post_params.sh
├── 6-peak.py
├── 6-peak.txt
├── 100-status_code.sh
├── 101-post_json.sh
└── 102-catch_me.sh
```

## Tasks

| Task Number | File Name         | Description                                                                                     |
|-------------|-------------------|-------------------------------------------------------------------------------------------------|
| 0           | 0-body_size.sh    | Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response. |
| 1           | 1-body.sh         | Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.             |
| 2           | 2-delete.sh       | Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response. |
| 3           | 3-methods.sh      | Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.    |
| 4           | 4-header.sh       | Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response with a custom header. |
| 5           | 5-post_params.sh  | Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response with POST parameters. |
| 6           | 6-peak.py         | Write a function that finds a peak in a list of unsorted integers. | 
| 6           | 6-peak.txt        | Contain the complexity of your algorithm. | 
| 7           | 100-status_code.sh| Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response. |
| 8           | 101-post_json.sh  | Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response. |
| 9           | 102-catch_me.sh   | Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response. |

## C Scripts
N/A

## Author
**Ifeanyi I Ekezie**  
[GitHub](https://github.com/iiekezie)
