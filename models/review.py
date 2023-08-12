#!/usr/bin/python3
"""Module defining the Feedback class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Symbolizes a feedback or comment left by a user for a place.

    Public class attributes:
        location_id (str): The ID related to a specific location; initialized as an empty string, expected to be replaced by Place.id later.
        commenter_id (str): The ID of the user leaving feedback; initialized as an empty string, expected to be replaced by User.id later.
        message (str): The actual feedback text left by the user.
    """
    place_id = ""
    user_id = ""
    text = ""
