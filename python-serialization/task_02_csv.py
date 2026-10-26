#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Reads a CSV file using a DictReader and seralises the data
    into a JSON fomrat saved as 'data.json'
    """
    try:
        # open and read csv file
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = lists(reader)

        #seralise and write list of dict
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except (FileNotFoundError, Exception):
        return False
