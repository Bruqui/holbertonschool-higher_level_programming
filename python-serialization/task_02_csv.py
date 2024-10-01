#!/usr/bin/python3
"""
This module provides a function to convert CSV data into JSON format.
It reads data from a CSV file and writes the equivalent JSON data to
data.json.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file.
    Args:
        csv_filename (str): The name of the CSV file to read data from.
    Returns:
        bool: True if the conversion was successful, False otherwise.
    Raises:
        FileNotFoundError: If the specified CSV file does not exist.
    """
    try:
        with open(csv_filename, mode='r', newline='',
                  encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
