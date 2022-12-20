#!/usr/bin/python3
"""A module for working with squares.
"""


class Square:
    """Represents a 2D Polygon with 4 equal and perpendicular sides.
    """
    def __init__(self, size=0):
        """Initializes a Square with a given size.
        Args:
            size (int): The size of the square.
        """
        super().__init__()
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

    def area(self):
        """Computes the area of this Square.
        Returns:
            int: The area of the Square.
        """
        return self.__size ** 2
