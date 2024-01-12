#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    n_list = my_list.copy()

    if idx < 0:
        return n_list
    elif idx >= length:
        return n_list
    else:
        n_list[idx] = element
        return n_list
