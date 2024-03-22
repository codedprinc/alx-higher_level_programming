#!/usr/bin/python3
""" 6. Create object from a JSON file """

import json

def load_from_json_file(filename=""):
    """
    creates an Object from a JSON file
    """

    with open(filename, encoding='utf-8') as fl:
        data = fl.read()

        return json.loads(data)
