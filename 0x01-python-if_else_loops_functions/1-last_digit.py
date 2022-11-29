#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > -1:

    n = number
    d = number % 10

    if number == 0:
        print(f"Last digit of {n} is {d} and is 0")
    elif number > 5:
        print(f"Last digit of {n} is {d} and is greater than 5")
    else:
        print(f"Last digit of {n} is {d} and is less than 6 and not 0")

elif number < 0:

    n = number
    d = -((number * -1) % 10)

    if number == 0:
        print(f"Last digit of {n} is {d} and is 0")
    elif number > 5:
        print(f"Last digit of {n} is {d} and is greater than 5")
    else:
        print(f"Last digit of {n} is {d} and is less than 6 and not 0")
