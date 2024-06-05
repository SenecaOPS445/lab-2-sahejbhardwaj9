#!/usr/bin/env python3



import sys

# Check if command line argument is provided
if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer -= 1

print("blast off!")
