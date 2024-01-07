#!/usr/bin/python3
invest , int_rate = input("Enter your investment and expected interest rate: ").split()
invest = float(invest)
int_rate = float(int_rate) * .01
for i in range(1,11):
    invest = invest + (invest * int_rate) #or interest = interest + ( interest * interest_rate)
print("Your earnings after a 10 year period: {:.2f}".format(invest))
