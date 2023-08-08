#!/usr/bin/python3
"""Definition of the CoreModel class."""
import models
from uuid import uuid4
from datetime import datetime

class CoreModel:
    """Symbolizes the CoreModel of the project."""

    def __init__(self, *init_args, **init_kwargs):
        """Create a new CoreModel.

        Args:
            *init_args (any): Not used.
            **init_kwargs (dict): Attributes as key/value pairs.
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.model_id = str(uuid4())
        self.model_created_at = datetime.today()
        self.model_updated_at = datetime.today()
        if len(init_kwargs) != 0:
            for key, value in init_kwargs.items():
                if key == "model_created_at" or key == "model_updated_at":
                    self.__dict__[key] = datetime.strptime(value, t_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def store(self):
        """Update model_updated_at with the current datetime and store the instance."""
        self.model_updated_at = datetime.today()
        models.storage.store()

    def to_dictionary(self):
        """Return the dictionary of the CoreModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        response_dict = self.__dict__.copy()
        response_dict["model_created_at"] = self.model_created_at.isoformat()
        response_dict["model_updated_at"] = self.model_updated_at.isoformat()
        response_dict["__class__"] = self.__class__.__name__
        return response_dict

    def __str__(self):
        """Return the print/str representation of the CoreModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.model_id, self.__dict__)
