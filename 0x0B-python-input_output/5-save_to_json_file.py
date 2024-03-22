#!/usr/bin/python3
"""
5. Save Object to a file

"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation

    """

    with open(filename, 'w', encoding='utf-8') as fl:
        data = json.dumps(my_obj)

        fl.write(data)
