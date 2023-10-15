#!/usr/bin/python3
"""
module serializing instances to JSON file
and deserializes JSON file to an instance
"""
import json


class FileStorage:
    """
    instance for storing and retrieving JSON strings
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        instance method that returns a dictionary of all objects stored in
        private class attribute '__objects'
        """

        return self.__objects

    def new(self, obj):
        """
        instance method that sets the '__objects' with the object argument
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serialize objects to json file in given path
        """

        temp = {}  # temporary dictionary to hold the values for each item

        for key, value in self.__objects.items():
            temp[key] = value.to_dict()

        # save the dictionary as a json file
        with open(self.__file_path, "w", encoding="utf-8") as file_write:
            file_write.write(json.dumps(temp))

    def reload(self):
        """
        deserializes JSON file to '__objects' attribute
        """
        # import the required modules
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        try:
            # open the file as read only
            with open(self.__file_path, "r", encoding="utf-8") as file_read:
                temp = json.loads(file_read.read())  # load the json string
                self.__objects = {}  # initialize it as empty
                # create objects from the json file extracts
                for key, value in temp.items():
                    # get name of class and construct the object from it
                    self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
