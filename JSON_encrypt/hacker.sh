#!/bin/bash

#This is basically how you create JSON using bash scripting.

# Variables
email= "rgangava@asu.edu"
legal_name= "Rohan Samuel Gangavarapu"
handle= "broke_boy@cse545"

# Creating JSON format
json_string=$(cat <<- EOM
{
    "email": "$email",
    "legal_name": $legal_name,
    "handle": "$handle"
}
EOM
)

# Echo JSON to a file
echo "$json_string" > output.json

# Print to console
echo "$json_string"
