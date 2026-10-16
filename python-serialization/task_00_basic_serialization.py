#!/usr/bin/env python3
"""handle data serialisation/deseralistion"""
import json

def serialize_and_save_to_file(data, filename):
    """Seralise a json file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """deseraliases JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
