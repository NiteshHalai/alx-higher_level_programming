#!/usr/bin/python3
def common_elements(set_1, set_2):
    uniques = []

    for i in set_1:
        if i in set_2:
            uniques.append(i)

    return uniques
