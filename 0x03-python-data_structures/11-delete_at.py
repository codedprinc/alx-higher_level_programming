#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    n_list = my_list.copy()
    l_list = []

    if idx < 0 or idx >= length:
        return n_list
    else:
        temp = n_list[idx]
        for i in range(length):
            if n_list[i] != temp:
                l_list.append(n_list[i])

        return l_list
