#!/usr/bin/python3
"""Module defining a function to create an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
