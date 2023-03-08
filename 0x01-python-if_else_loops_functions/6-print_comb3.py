#!/usr/bin/python3

for i in range(0, 9):
    for k in range(i, 10):
        if i != k:
            print(f"{}, ".format(i, k), end="")
print('\n')
