#!/usr/bin/python3
"""
8. Class to JSON

"""
import json

def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    return json.dumps(obj)
