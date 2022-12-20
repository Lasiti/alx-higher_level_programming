#!/usr/bin/python3
"""A module for working with squares.
"""


class Square:
    """Represents a 2D Polygon with 4 equal and perpendicular sides.
    """
    def __init__(self, size):
        """Initializes a Square with a given size.
        Args:
            size (int): The size of the square.
        """
        super().__init__()
        self.__size = size
