#!/usr/bin/python3
"""
Module for class User inheriting from the BaseModel class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A User class inheriting from the BaseModel class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
