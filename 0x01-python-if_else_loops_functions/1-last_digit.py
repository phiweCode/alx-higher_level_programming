#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10

if number == 0:
    print(f"Last digit of {number} is {lastDigit} and is 0", end="\n")

if number > 5:
    print(f"Last digit of {number} is {lastDigit} greater than 5", end="\n")

if number < 6 and number != 0:
    print(f"Last digit of {number} is {lastDigit} ", end="")
    print(f"and is less than 6 and not 0", end="\n")
