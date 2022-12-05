#!/usr/bin/python3
def no_c(my_string):
    new = []
    for i in my_string:
        if i not in ['c', 'C']:
            new.append(i)

    new = ''.join(new)

    return new
