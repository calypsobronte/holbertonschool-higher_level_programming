#!/usr/bin/python3
""" Base
"""

import json
import csv


class Base:
    """Base Class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a given list of dictionaries to a json string."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs."""
        if list_objs is None:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
        with open(cls.__name__ + ".json", "w") as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation."""
        if json_string is None or "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        test = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        test.update(**dictionary)
        return test

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                pass
        except FileNotFoundError:
            return []
        with open(cls.__name__ + ".json", "r") as f:
            ld = cls.from_json_string(f.read())
            return [cls.create(**d) for d in ld]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save objs as csv files"""
        if cls.__name__ == "Rectangle":
            head = "id,width,height,x,y"
        elif cls.__name__ == "Square":
            head = "id,size,x,y"
        save_obj = ""
        for obj in list_objs:
            obj = obj.to_dictionary()
            attrs = head.split(",")
            save_obj += ",".join([str(obj[key]) for key in attrs])
            save_obj += "\n"
        string = "\n".join([head, save_obj])
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            file.write(string)

    @classmethod
    def load_from_file_csv(cls):
        """load objs from csv files"""
        name = cls.__name__
        with open(name + ".csv", "r") as f:
            cont = f.read().split("\n")
            objs = []
            for obj in cont[1:-1]:
                objs.append(obj.split(","))
            array = []
            for obj in objs:
                if name == "Rectangle":
                    attrs = ["id", "width", "height", "x", "y"]
                elif name == "Square":
                    attrs = ["id", "size", "x", "y"]
                dic = {key: int(obj[i].strip()) for i, key in enumerate(attrs)}
                array.append(cls.create(**dic))
            return array
