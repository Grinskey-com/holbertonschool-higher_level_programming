#!/usr/bin/env python3
"""pickle method"""
import pickle


class CustomObject:
    """custom object class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """method to print attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """method to serialise"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self,f)
        except Exception:
            return None
    @classmethod
    def deserialize(cls, filename):
        """method to deserialise"""
        try:
            with open(filename,'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
