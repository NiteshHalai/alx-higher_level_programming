#!/usr/bin/python3


"""Function description here"""

import json


def load_from_json_file(filename):
    """Function description here"""

    with open(filename, encoding="utf-8") as f:
        json_str = f.read()

    return json.loads(json_str)
