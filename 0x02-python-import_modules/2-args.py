#!/usr/bin/python3

import sys

length = len(sys.argv)

print(f"{length}")

if length > 0:

    for i in range(length):
        print("{i}: {sys.argv[i]}")
elif length == 0:
    print("0 arguments")