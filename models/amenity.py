#!/usr/bin/python3
"""
class Amenity that inherits from BaseModel class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Manages attributes of Amenities
    Inherits attributes of BaseModel Class
    """

    name = ""
