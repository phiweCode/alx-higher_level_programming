#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lastDigit = ((number * -1) % 10) * -1
else:
    lastDigit = number % 10

if lastDigit == 0:
    print(f"Last digit of {number} is {lastDigit} and is 0", end="\n")

elif lastDigit > 5:
    print(f"Last digit of {number} is {lastDigit}", end="")
    print(f" and is greater than 5", end="\n")

elif lastDigit < 6 and number != 0:
    print(f"Last digit of {number} is {lastDigit} ", end="")
    print(f"and is less than 6 and not 0", end="\n")
