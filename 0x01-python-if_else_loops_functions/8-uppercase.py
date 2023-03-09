#!/usr/bin/python3

def uppercase(str):

    for i in range(0, len(str)):
        ascAlp = ord(str[i])

        print(f"""{chr(ascAlp - 32) if ascAlp >= 97
        else chr(ascAlp)}""", end="")

    print('\n')
