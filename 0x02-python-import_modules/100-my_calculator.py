#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

arguments = sys.argv
operators = ['+', '-', '*', '/']

if len(arguments) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if arguments[2] not in operators:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
if arguments[2] == '+':
    print("{} + {} = {}".format(arguments[1], arguments[3], add(int(arguments[1]),int(arguments[3]))
    exit(0)
if arguments[2] == '-':
    print("{} - {} = {}".format(arguments[1], arguments[3], sub(int(arguments[1]),int(arguments[3]))
    exit(0)
if arguments[2] == '*':
    print("{} * {} = {}".format(arguments[1], arguments[3], mul(int(arguments[1]),int(arguments[3]))
    exit(0)
if arguments[2] == '/':
    print("{} / {} = {}".format(arguments[1], arguments[3], div(int(arguments[1]),int(arguments[3]))
    exit(0)
