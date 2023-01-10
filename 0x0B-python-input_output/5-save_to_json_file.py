#!/usr/bin/python3


"""Function description here"""

import json


def save_to_json_file(my_obj, filename):
    """Function description here"""
    json_str = json.dumps(my_obj)
    
    with open(filename, encoding="utf-8", mode="w") as f:
        return f.write(json_str)
