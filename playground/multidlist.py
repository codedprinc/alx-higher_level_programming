#!/usr/bin/python3
if __name__ == "__main__":
    import random
    import math

    multitable = [[0] * 10 for i in range(10)]

    for i in range(1, 10):
        for j in range(1, 10):
            multitable[i][j] =  "{}".format((i * j))

    for i in range(1, 10):
        for j in range(1, 10):
            print(multitable[i][j], end=", ")
        print()
