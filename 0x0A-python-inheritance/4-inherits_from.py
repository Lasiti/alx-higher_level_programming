#!/usr/bin/python3
'''A module for inspecting an object.
'''


def inherits_from(obj, a_class):
    '''Checks if an object inherited from the specified class.
    Args:
        obj (any): an object to be checked.
        a_class (any): A class to be compared against.
    Returns:
        bool: True if `obj` is an inheritance of `a_class`.
    '''
    return issubclass(obj.__class__, a_class) and (type(obj) is not a_class)
