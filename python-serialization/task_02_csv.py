#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Reads a CSV file using a DictReader and seralises the data
    into a JSON fomrat saved as 'data.json'
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = lists(reader)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except (FileNotFoundError, Exception):
        return False
