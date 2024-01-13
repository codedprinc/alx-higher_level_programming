#!/usr/bin/python3
def no_c(my_string):
    strcp = my_string
    result = ''

    for wd in strcp:
        if wd != 'c' and wd != 'C':
            result += wd

    return result
