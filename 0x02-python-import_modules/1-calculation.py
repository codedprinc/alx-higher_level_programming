#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
res0 = add(a, b)
res1 = sub(a, b)
res2 = mul(a, b)
res3 = div(a, b)

if __name__ = "__main__":
    print("{0} + {1} = {2:d}".format(a, b, res0))
    print("{0} - {1} = {2:d}".format(a, b, res1))
    print("{0} * {1} = {2:d}".format(a, b, res2))
    print("{0} / {1} = {2:d}".format(a, b, res3))
