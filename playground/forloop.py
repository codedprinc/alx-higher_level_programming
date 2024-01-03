#!/usr/bin/python3
#print odds from 1 - 20
#use a for loop and range and use if and modulus to print out the odds.
for i in range(20):
    if (i % 2) != 0:
        print("{} is an odd number".format(i))
    else:
        print("{} is even".format(i))

print('done') 
