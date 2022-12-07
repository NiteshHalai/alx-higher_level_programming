#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniques = []
    total = 0

    for i in my_list:
        if i not in uniques:
            uniques.append(i)
            total = total + i

    return total
