#!/usr/bin/python3
import pickle

def serialize_and_save_to_file(data, filename):
    """
    Serialize the given data and save it to a file.
    Args:
        data (Any): The Python object to be serialized.
        filename (str): The name of the file where the serialized data will
        be stored.
    """
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_and_deserialize(filename):
    """
    Load and deserialize data from a file.
    Args:
        filename (str): The name of the file from which the serialized data
        will be loaded.
    Returns:
        Any: The deserialized Python object.
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)