#!/usr/bin/python3
"""
Square Calss
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the height"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if args:
            attr = ['id', 'size', 'x', 'y']
            for i, e in enumerate(args):
                setattr(self, attr[i], e)
            return
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
            }
