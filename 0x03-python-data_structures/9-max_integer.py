#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        i = len(my_list) - 1
        k = i
        while i > 1:
            j = 0
            while j < i:
                if my_list[j] > my_list[j + 1]:
                    temp = my_list[j]
                    my_list[j] = my_list[j + 1]
                    my_list[j + 1] = temp
                j += 1
            i -= 1

        ans = my_list[k]
    return ans
