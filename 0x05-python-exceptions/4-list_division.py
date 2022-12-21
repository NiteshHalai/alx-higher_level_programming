#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_3 = []
    for i in range(0, list_length):
        try:
            list_3.append(my_list_1[i]/my_list_2[i])
        except Exception:
            ValueError
        finally:
            pass

    return list_3
