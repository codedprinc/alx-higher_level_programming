#!/usr/bin/python3
def element_at(my_list, idx):
    l = len(my_list)
    if idx < 0:
        return None
    elif idx > l:
        return None
    elif idx >= 0:
        ans = "{}".format(my_list[idx])
        return ans
