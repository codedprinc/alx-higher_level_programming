#!/usr/bin/python3

from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s1.update(1, 2, 4, 5)
    print(s1)
