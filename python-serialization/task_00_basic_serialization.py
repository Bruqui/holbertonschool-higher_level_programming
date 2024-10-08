#!/usr/bin/python3
"""
This module provides basic serialization and deserialization functionality.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize the given data and save it to a file.
    Args:
        data (Any): The Python object to be serialized.
        filename (str): The name of the file where the serialized data will
        be stored.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a file.
    Args:
        filename (str): The name of the file from which the serialized data
        will be loaded.
    Returns:
        Any: The deserialized Python object.
    """
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        return data
