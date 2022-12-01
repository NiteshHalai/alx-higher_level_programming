#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    
arguments = sys.argv

if len(arguments) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    print(1)
