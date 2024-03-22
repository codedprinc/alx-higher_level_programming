#!/usr/bin/python3
""" 1.Write to a file"""

def write_file(filename="", text=""):
    """
    Writes a string to a trxt file(`UTF-8`)
    and returns the number of characters written

    """

    with open(filename, 'w', encoding="utf-8") as fl:
        return fl.write(text)
