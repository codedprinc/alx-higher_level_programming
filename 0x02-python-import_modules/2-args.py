#!/usr/bin/python3
import sys
n = len(sys.argv) - 1

if n == 0:
    print("{} arguments.".format(n))
elif n == 1:
    print("{} argument:".format(n))
elif n > 1:
    print("{} arguments:".format(n))

for y in range(1, n):
    print("{0} : {1}".format(y, sys.argv[y]))
