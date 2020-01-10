#!/usr/bin/python3
class Square:
    """ class square with function of size private attribute """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, size=0):
        if (type(size) is not tuple or len(size) is not 2 or
            type(size[0]) is not int or type(size[1]) is not int or
                size[0] < 0 or size[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size != 0:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                if self.__position[0]:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print("")
