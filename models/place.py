#!/usr/bin/python3
"""
Module for the Location class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """A class that inherits from the BaseModel

     Attributes:
        city_id (str): The id of the locale
        user_id (str): The id of the owner
        name (str): The name of the location
        description (str): The details of the location
        number_rooms (int): The total number of rooms in the location
        number_bathrooms (int): The total number of bathrooms in the location
        max_gues (int): The maximum number of guests in the location
        price_by_night (int): The nightly rate for the location
        latitude (float): The latitude of the location
        longitude (float): The longitude of the location
        amenity_ids (list): A list of ids for the features of the location

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
