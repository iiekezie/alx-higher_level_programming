#!/usr/bin/python3
"""Script to add arguments to a Python list and save them to a JSON file"""

import sys
import json
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# File to save the list
filename = "add_item.json"

# Check if the file exists, if not create it
if not path.exists(filename):
    save_to_json_file([], filename)

# Load the existing list from the file
my_list = load_from_json_file(filename)

# Add all arguments to the list
for arg in sys.argv[1:]:
    my_list.append(arg)

# Save the updated list back to the file
save_to_json_file(my_list, filename)
