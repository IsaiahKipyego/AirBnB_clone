#!/usr/bin/python3
"""
Defines common attributes for other classes
It is base class for all classes that inherit from it
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class for all classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor initializes instance attributes
        """
        if kwargs:
            my_format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, my_format)
                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        instance method for defining string output
        """
        string = "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                       self.__dict__)
        return (string)

    def save(self):
        """
        An instance method seting updated time of class instance
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        instance method that converts object to a dictionary format
        """
        output = self.__dict__.copy()
        output['__class__'] = self.__class__.__name__
        output['created_at'] = self.created_at.isoformat()
        output['updated_at'] = self.updated_at.isoformat()
        return (output)
