#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays:
- The body of the response if there are no errors
- The error code when there is an HTTP error.
"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
