#!/usr/bin/python3
# ------PROBLEM--------
# Find the multiples of 9 from a random 100 value list with values
# between 1 and 1000
import random

randlist = list(random.randint(1, 1001) for i in range(100))

print(list(filter((lambda x: x % 9 == 0), randlist)))
