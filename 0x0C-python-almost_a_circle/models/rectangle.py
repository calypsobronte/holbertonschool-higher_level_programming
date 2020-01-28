#!/usr/bin/python3
"""
Rectangle Class.
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the class."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the widht."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the widht."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area value of Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Prints in stdout Rectangle instance with character #."""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update class Rectangle with public method."""
        atts = ["id", "width", "height", "x", "y"]
        [setattr(self, a, b) for a, b in zip(atts, args)]
        [setattr(self, a, b) for a, b in kwargs.items()]

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        obj = self.__dict__
        attrs = ["id", "width", "height", "x", "y"]
        obj = {key: getattr(self, key) for key in attrs}
        return obj