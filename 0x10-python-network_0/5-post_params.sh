#!/bin/bash

# Check if argument is provided
if [ $# -eq 0 ]; then
	    echo "Usage: $0 <URL>"
	        exit 1
fi

url=$1

# Send POST request with parameters
curl -sSL -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$url"
