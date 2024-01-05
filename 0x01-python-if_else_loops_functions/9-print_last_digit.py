#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        l_n = (number * -1) % 10
    elif number >= 0:
        l_n = number % 10
    print("{:d}".format(l_n), end="")
    return l_n
