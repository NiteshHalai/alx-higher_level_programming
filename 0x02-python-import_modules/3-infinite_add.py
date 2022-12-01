#!/usr/bin/python3
if __name__ == "__main__":
    import sys

arguments = sys.argv
total = 0
for i in range(1, len(arguments) - 1):
    total = total + int(arguments[i])

print(total)
