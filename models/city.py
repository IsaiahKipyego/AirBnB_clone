#!/usr/bin/python3
"""
class City that inherits from BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class to manage Cities
    Inherits attributes of BaseModel Class
    """

    state_id = ""
    name = ""
