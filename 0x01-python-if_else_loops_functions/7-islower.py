#!/usr/bin/python3
def islower(c):
    num = ord(c)
    if num >= 97 and num <= 122:
        return True
    elif num >= 65 and num <= 90:
        return False
