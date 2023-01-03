#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value+0))
        return True
    except Exception:
        return False
