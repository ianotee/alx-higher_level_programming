#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """A student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a  Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A dictionary  representation of the Student"""
        return self.__dict__
