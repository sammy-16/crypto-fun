#!/bin/bash

# Check if the hacker.json file exists in the current directory
if [[ -f "hacker.json" ]]; then
    # Use the zip command to compress the hacker.json file
    zip hacker.zip hacker.json
    
    # Inform the user that the operation was successful
    echo "Successfully compressed hacker.json into hacker.zip."
else
    # Inform the user that the hacker.json file was not found
    echo "Error: hacker.json not found."
fi
