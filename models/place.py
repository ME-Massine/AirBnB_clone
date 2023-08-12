#!/usr/bin/python3
"""
Module for the Location class
"""
from models.base_model import BaseModel


class Location(BaseModel):
    """A class that inherits from the BaseModel

     Attributes:
        locale_id (str): The id of the locale
        owner_id (str): The id of the owner
        location_name (str): The name of the location
        details (str): The details of the location
        total_rooms (int): The total number of rooms in the location
        total_bathrooms (int): The total number of bathrooms in the location
        guest_capacity (int): The maximum number of guests in the location
        nightly_rate (int): The nightly rate for the location
        lat (float): The latitude of the location
        lon (float): The longitude of the location
        feature_ids (list): A list of ids for the features of the location

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
