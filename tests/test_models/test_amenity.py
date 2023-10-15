#!/usr/bin/python3
"""
Amenity class test module
"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    class that tests Amenity class which inherits from BaseModel
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
        executed last after all tests have been done
        """
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_init(self):
        """
        tests if class is instantiated and inherits correctly
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)
        # instantiate with argument
        amenity = Amenity(45)
        self.assertIsInstance(amenity, Amenity)
        self.assertFalse(hasattr(amenity, "45"))

    def test_init_kwargs(self):
        """
        Pass key worded args as parameters
        """

        amenity = Amenity(name="Lennox")
        self.assertIsInstance(amenity, Amenity)

        # multiple arguments
        amenity = Amenity(name="Lennox", name2="Fred")

    def test_attributes(self):
        """
        test if main class Attributes exist
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, "name"))
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "__class__"))
        self.assertFalse(hasattr(amenity, "Lennox"))

    def test_to_dict(self):
        """
        test inherited to dict method
        """
        amenity_1 = Amenity()
        amenity_2 = Amenity()
        test = amenity_1.to_dict()
        self.assertIsInstance(amenity_1, Amenity)
        self.assertEqual(type(amenity_1).__name__, "Amenity")
        self.assertEqual(test['__class__'], "Amenity")
        self.assertTrue(type(test['created_at']), 'str')
        self.assertNotEqual(amenity_1.id, amenity_2.id)

    def test_str(self):
        """
        test if __str__ method is working as expected
        """
        amenity = Amenity()
        check = "[{}] ({}) {}".format(amenity.__class__.__name__, amenity.id,
                                      amenity.__dict__)
        out = amenity.__str__()
        self.assertEqual(check, out)


if __name__ == '__main__':
    unittest.main()
