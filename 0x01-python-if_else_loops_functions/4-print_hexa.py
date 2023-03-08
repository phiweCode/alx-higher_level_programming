#!/usr/bin/python3

counter = 0
alp = 97
tens = 0

for i in range(0, 99):

    if counter < 10:
        print(f"{i} = 0x{'' if tens == 0 else tens}{counter}")
        counter += 1

    elif counter >= 10:
        print(f"{i} = 0x{'' if tens == 0 else tens}{chr(alp)}")
        alp += 1
        counter += 1

        if counter == 16:
            alp = 97
            counter = 0
            tens += 1
