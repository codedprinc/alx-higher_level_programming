#!/usr/bin/python3
""" 1- main"""
from models.rectangle import Rectangle


if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1.id)

    r1.display()

    print("---")

    r2 = Rectangle(4, 6)
    r2.display()
