#!/usr/bin/python3
"""Defines the DiskStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DiskStorage:
    """Symbolizes an abstract storage engine.

    Attributes:
        __storage_path (str): The name of the file to save objects to.
        __storage_objects (dict): A dictionary of instantiated objects.
    """
    __storage_path = "storage.json"
    __storage_objects = {}

    def retrieve_all(self):
        """Return the dictionary __storage_objects."""
        return DiskStorage.__storage_objects

    def add_new(self, obj):
        """Set in __storage_objects obj with key <obj_class_name>.id"""
        class_name = obj.__class__.__name__
        DiskStorage.__storage_objects["{}.{}".format(class_name, obj.id)] = obj

    def store(self):
        """Serialize __storage_objects to the JSON file __storage_path."""
        object_dict = DiskStorage.__storage_objects
        serial_objects = {obj: object_dict[obj].to_dict() for obj in object_dict.keys()}
        with open(DiskStorage.__storage_path, "w") as file:
            json.dump(serial_objects, file)

    def load(self):
        """Deserialize the JSON file __storage_path to __storage_objects, if it exists."""
        try:
            with open(DiskStorage.__storage_path) as file:
                serial_objects = json.load(file)
                for obj in serial_objects.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.add_new(eval(class_name)(**obj))
        except FileNotFoundError:
            raise FileNotFoundError("File not found: {}".format(DiskStorage.__storage_path))
