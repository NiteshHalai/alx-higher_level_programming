#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number == 0:
    print("Last of digit of {number:d} is {number % 10:d} and is 0")
else if number > 5:
    print("Last of digit of {number:d} is {number % 10:d} and is greater than 5")
else:
    print("Last of digit of {number:d} is {number % 10:d} and is less than 6 and not 0")
