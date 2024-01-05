#!/usr/bin/python3
def uppercase(str):
    for i in str:
        num = ord(i)
        if num >= 97 and num <= 122:
            i = chr(num - 32)
        print("{:s}".format(i), end='')
    print()
