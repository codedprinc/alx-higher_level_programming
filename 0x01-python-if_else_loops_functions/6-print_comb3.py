#!/usr/bin/python3
for num in range(0, 10):
    for j in range((num + 1), 10):
        if num != j:
            if num == 8 and j == 9:
                print("{0}{1}".format(num, j), end=' ')
            else:
                print("{0}{1}".format(num, j), end=', ')
#print("\n")
