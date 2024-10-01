#!/usr/bin/python3
"""
This module provides functions to serialize a Python dictionary into XML
format and deserialize it back into a dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.
    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file where the XML data will be saved.
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file into a Python dictionary.
    Args:
        filename (str): The name of the file to read XML data from.
    Returns:
        dict: A dictionary representation of the XML data.
    """    
    tree = ET.parse(filename)
    root = tree.getroot()
    result_dict = {}
    for child in root:
        result_dict[child.tag] = child.text
    return result_dict
