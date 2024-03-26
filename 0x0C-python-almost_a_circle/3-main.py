#!/usr/bin/python3

from models.rectangle import Rectangle

if __name__ == '__main__':

    r1 = Rectangle(10, 3, 5, 7)
    r2 = Rectangle(2, 6)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())
