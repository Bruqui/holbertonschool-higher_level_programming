#!/usr/bin/python3
"""
This module provides basic serialization and deserialization functionality.
It allows serializing a Python dictionary into a JSON file and deserializing
JSON data from a file back into a Python dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file and saves it.
    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The filename where the serialized data will be saved.
        If the file already exists, it will be replaced.
    Raises:
        IOError: If there is an error writing to the file.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Data has been serialized and saved to '{filename}'.")
    except IOError as e:
        print(f"An error occurred while saving data to '{filename}': {e}")


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file back into a Python dictionary
    Args:
        filename (str): The name of the file containing the JSON data.
    Returns:
        dict: A Python dictionary with the deserialized data.
    Raises:
        IOError: If there is an error reading from the file.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except IOError as e:
        print(f"An error occurred while loading data from '{filename}': {e}")
    except json.JSONDecodeError as e:
        print(f"An error occurred while decoding JSON from '{filename}': {e}")
