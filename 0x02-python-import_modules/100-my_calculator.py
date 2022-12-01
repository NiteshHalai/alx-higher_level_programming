#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

a = sys.argv
operators = ['+', '-', '*', '/']

if len(a) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if a[2] not in operators:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
if a[2] == '+':
    print("{} + {} = {}".format(a[1], a[3], add(int(a[1]), int(a[3]))))
    exit(0)
if a[2] == '-':
    print("{} - {} = {}".format(a[1], a[3], sub(int(a[1]), int(a[3]))))
    exit(0)
if a[2] == '*':
    print("{} * {} = {}".format(a[1], a[3], mul(int(a[1]), int(a[3]))))
    exit(0)
if a[2] == '/':
    print("{} / {} = {}".format(a[1], a[3], div(int(a[1]), int(a[3]))))
    exit(0)
