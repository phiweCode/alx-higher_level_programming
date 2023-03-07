#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number == 0:
    print("0 is zero", end="\n")
elif number < 0:
    print(f"{number} is negative", end="\n")
else:
    number > 0
    print(f"{number} is positive", end="\n")
