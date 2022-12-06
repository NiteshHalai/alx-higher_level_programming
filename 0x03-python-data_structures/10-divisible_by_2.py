#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    test = []
    for j in my_list:
        if j % 2 == 0:
            test.append(True)
        else:
            test.append(False)

    return test
