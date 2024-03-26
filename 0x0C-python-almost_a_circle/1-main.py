#!/usr/bin/python3
""" 1- main"""
from models.rectangle import Rectangle


if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1)
    print("_____")
    r_d = r1.to_dictionary()
    print(r_d)
#    r1.update(32)
    print(r1)

    print("_____")
    r1.update(50, 234, 50)
    print(r1)

 #   r1.display()

    print("---")

    r2 = Rectangle(4, 6)
#    r2.display()

    print("-------*---")
    print(r2)
