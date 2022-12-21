#!/usr/bin/python3
"""Define a class Square."""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """set the current size of the square."""
        return(self.__self)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def postion(self):
        """set the current position of the square."""
        return(self.__postion)
    @postion.setter
    def area(self):
        return(self.__size * self.__size)
    def my_print(self):
        if self.__size == 0:
            print(" ")
            return

        [print("") for i in range(0, self.__postion[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(0, self.__postion[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
