#!/usr/bin/python3
# ---------PROBLEM---------------
# Create a random list filled with the characters H and T
# for heads and Tails. Output the number of Hs and Ts
# Example Output
# Heads : 46
# Tails : 54

import random
fliplist = []

for i in range(1, 1001):
    fliplist += random.choice(['H', 'T'])

print("Heads :", fliplist.count('H'))
print("Tails :", fliplist.count('T'))
