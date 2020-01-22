#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        array = {}
        if attrs is None:
            return self.__dict__
        else:
            for cont in attrs:
                if cont in self.__dict__:
                    array[cont] = self.__dict__[cont]

        return array
