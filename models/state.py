#!/usr/bin/python3
"""
class State inheriting from the BaseModel class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Manages attributes of the States
    Inherits attributes of the BaseModel Class
    """

    name = ""
