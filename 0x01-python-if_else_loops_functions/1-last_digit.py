#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > -1:
    if number == 0:
        print(f"Last digit of {number:d} is {number % 10:d} and is 0")
    elif number > 5:
        print(f"Last digit of {number:d} is {number % 10:d} and is greater than 5")
    else:
        print(f"Last digit of {number:d} is {number % 10:d} and is less than 6 and not 0")
        
elif number < 0:
    
    d = -((number * -1) % 10)
    
    if number == 0:
        print(f"Last digit of {number} is {d} and is 0")
    elif number > 5:
        print(f"Last digit of {number} is {d} and is greater than 5")
    else:
        print(f"Last digit of {number} is {d} and is less than 6 and not 0")
