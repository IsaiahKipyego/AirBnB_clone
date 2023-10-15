#!/usr/bin/python3
"""
test module for City class
"""
import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    classthat tests State class which inherits from BaseModel
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
        tests if class is instantiated and inherits correctly
        """
        obj = City()
        self.assertIsInstance(obj, City)
        self.assertIsInstance(obj, BaseModel)
        # instantiate with argument
        obj = City(45)
        self.assertIsInstance(obj, City)
        self.assertFalse(hasattr(obj, "45"))

    def test_init_kwargs(self):
        """
        pass key worded args as parameters
        """

        obj = City(name="Lennox")
        self.assertIsInstance(obj, City)

        # multiple arguments
        obj = City(name="Lennox", name2="Fred")

    def test_attributes(self):
        """
        test whether main class Attributes exist
        """
        obj = City()
        self.assertIsInstance(obj, City)
        self.assertTrue(hasattr(obj, "name"))
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "__class__"))
        self.assertFalse(hasattr(obj, "Lennox"))
        self.assertTrue(hasattr(obj, "state_id"))

    def test_to_dict(self):
        """
        test inherited to dict method
        """
        obj_1 = City()
        obj_2 = City()
        test = obj_1.to_dict()
        self.assertIsInstance(obj_1, City)
        self.assertEqual(type(obj_1).__name__, "City")
        self.assertEqual(test['__class__'], "City")
        self.assertTrue(type(test['created_at']), 'str')
        self.assertNotEqual(obj_1.id, obj_2.id)

    def test_str(self):
        """
        test if  __str__ method is working as expected
        """
        obj = City()
        check = "[{}] ({}) {}".format(obj.__class__.__name__, obj.id,
                                      obj.__dict__)
        out = obj.__str__()
        self.assertEqual(check, out)


if __name__ == '__main__':
    unittest.main()
