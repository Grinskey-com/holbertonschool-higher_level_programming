#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialises a Python dictionary into an XML file using ElementTree.
    """
    root = ET.Element('data')
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Parses an XML file and reconstructs it into a Python dict.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        reconstructed_dict = {}
        for child in root:
            reconstructed_dict[child.tag] = child.text
            
        return reconstructed_dict
    except (FileNotFoundError, ET.ParseError) as e:
        print(f"Error processing XML file: {e}")
        return None
    