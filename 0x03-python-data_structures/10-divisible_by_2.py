#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n_list = my_list.copy()
    length = len(n_list)
    i = 0

    while i < length:
        if n_list[i] % 2 == 0:
            n_list[i] = True
        else:
            n_list[i] = False
        i += 1

    return n_list
