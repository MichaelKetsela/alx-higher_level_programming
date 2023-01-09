#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Returns: If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    return (type(obj) == a_class)
