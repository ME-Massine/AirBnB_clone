#!/usr/bin/python3
"""
Module for the CustomFeature class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class representing Amenity of a location or property

    Attributes:
        name : amenity name

    """
    name = ""
