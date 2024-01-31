#!/usr/bin/python3
def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def change_list(list, func):
    oddlist = []
    for i in list:
        if func(i):
            oddlist.append(i)
    return oddlist

alist = range(1, 20)
print(change_list(alist, is_it_odd))
