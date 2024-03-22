#!/usr/bin/python3
""" 0. read file"""


def read_file(filename=""):
    """
    Reads a text file (`UTF8`) and prints to stdout

    """

    with open(filename, encoding="utf-8") as f:
        data = f.read()

        for line in data:
            print(line, end='')
