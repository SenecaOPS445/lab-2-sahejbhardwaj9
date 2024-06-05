#!/usr/bin/env python3


import sys

# Check if the number of arguments is exactly 3 (including the script name)
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()

# Assigning the first argument to the variable "name" and the second to "age"
name = sys.argv[1]
age = sys.argv[2]

print(f"Hi {name}, you are {age} years old.")
