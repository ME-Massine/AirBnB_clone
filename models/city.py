#!/usr/bin/python3
"""
Module for the city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class that represents a city

    Attributes:
        state_id (str): The id of the region
        name (str): The name of the locale

    """

    state_id = ""
    name = ""
