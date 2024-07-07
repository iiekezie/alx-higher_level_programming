#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q.
If no argument is given, set q="". If the response body is properly JSON
formatted and not empty, display the id and name like this:
[<id>] <name>. Otherwise:
- Display Not a valid JSON if the JSON is invalid
- Display No result if the JSON is empty
"""

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    try:
        response = requests.post(url, data={'q': q})
        json_response = response.json()

        if json_response:
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
    
    except Exception as e:
        print("No result")
