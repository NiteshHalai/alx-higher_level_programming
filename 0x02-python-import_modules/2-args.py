#!/usr/bin/python3
import sys
arguments = sys.argv

if len(arguments) == 1:
    print("0 arguments.")
elif len(arguments) == 2:
    print("1 argument:")
    print("1: {}".format(arguments[1]))
else:
    print("{} arguments:".format(len(arguments)))
    for i in range(0, len(arguments)):
        print("{}: {}".format(i, arguments[i]))
