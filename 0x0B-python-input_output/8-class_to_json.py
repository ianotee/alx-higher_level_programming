#!/usr/bin/python3
"""A Python class-to-JSON function"""


def class_to_json(obj):
    """A  dictionary representation of a  data structure"""
    return obj.__dict__
