#!/usr/bin/python3
"""
test module for the User class
"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    class tests the State class which inherits from BaseModel
    """

    def setUp(self):
        """
        executed first before any other tests
        """
        try:
            os.remove("file.json")
        except IOError:
            pass

    def tearDown(self):
        """
        executed last after all tests have been performed
        """
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_init(self):
        """
        if the class is instantiated and inherits correctly
        """
        obj = User()
        self.assertIsInstance(obj, User)
        self.assertIsInstance(obj, BaseModel)
        # instantiate with argument
        obj = User(45)
        self.assertIsInstance(obj, User)
        self.assertFalse(hasattr(obj, "45"))

    def test_init_kwargs(self):
        """
        pass key worded arguments as parameters
        """

        obj = User(name="Isaiah")
        self.assertIsInstance(obj, User)

        # multiple arguments
        obj = User(name="Isaiah", name2="Kipyego")

    def test_attributes(self):
        """
        test if main class Attributes exist
        """
        obj = User()
        self.assertIsInstance(obj, User)
        self.assertFalse(hasattr(obj, "name"))
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "__class__"))
        self.assertFalse(hasattr(obj, "Isaiah"))
        self.assertTrue(hasattr(obj, "email"))
        self.assertTrue(hasattr(obj, "password"))
        self.assertTrue(hasattr(obj, "first_name"))
        self.assertTrue(hasattr(obj, "last_name"))

    def test_to_dict(self):
        """
        test the inherited to dict method
        """
        obj_1 = User()
        obj_2 = User()
        test = obj_1.to_dict()
        self.assertIsInstance(obj_1, User)
        self.assertEqual(type(obj_1).__name__, "User")
        self.assertEqual(test['__class__'], "User")
        self.assertTrue(type(test['created_at']), 'str')
        self.assertNotEqual(obj_1.id, obj_2.id)

    def test_str(self):
        """
        test if __str__ method is working as expected
        """
        obj = User()
        check = "[{}] ({}) {}".format(obj.__class__.__name__, obj.id,
                                      obj.__dict__)
        out = obj.__str__()
        self.assertEqual(check, out)


if __name__ == '__main__':
    unittest.main()
