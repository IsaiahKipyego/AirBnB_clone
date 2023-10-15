#!/usr/bin/python3
"""
test module for Place class
"""
import unittest
import os
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    class that tests Place class which inherits from BaseModel
    """

    def setUp(self):
        """
        executed first before other tests
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
        obj = Place()
        self.assertIsInstance(obj, Place)
        self.assertIsInstance(obj, BaseModel)
        # instantiate with argument
        obj = Place(45)
        self.assertIsInstance(obj, Place)
        self.assertFalse(hasattr(obj, "45"))

    def test_init_kwargs(self):
        """
        pass key worded arguments as parameters
        """

        obj = Place(name="Isaiah")
        self.assertIsInstance(obj, Place)

        # multiple arguments
        obj = Place(name="Isaiah", name2="Kipyego")

    def test_attributes(self):
        """
        test if main class Attributes exist
        """
        obj = Place()
        self.assertIsInstance(obj, Place)
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "__class__"))
        self.assertFalse(hasattr(obj, "Isaiah"))
        self.assertTrue(hasattr(obj, "user_id"))
        self.assertTrue(hasattr(obj, "city_id"))
        self.assertTrue(hasattr(obj, "name"))
        self.assertTrue(hasattr(obj, "description"))
        self.assertTrue(hasattr(obj, "number_rooms"))
        self.assertTrue(hasattr(obj, "number_bathrooms"))
        self.assertTrue(hasattr(obj, "max_guest"))
        self.assertTrue(hasattr(obj, "price_by_night"))
        self.assertTrue(hasattr(obj, "latitude"))
        self.assertTrue(hasattr(obj, "longitude"))
        self.assertTrue(hasattr(obj, "amenity_ids"))

    def test_to_dict(self):
        """
        test inherited to dict method
        """
        obj_1 = Place()
        obj_2 = Place()
        test = obj_1.to_dict()
        self.assertIsInstance(obj_1, Place)
        self.assertEqual(type(obj_1).__name__, "Place")
        self.assertEqual(test['__class__'], "Place")
        self.assertTrue(type(test['created_at']), 'str')
        self.assertNotEqual(obj_1.id, obj_2.id)

    def test_str(self):
        """
        test if __str__ method is working as expected
        """
        obj = Place()
        check = "[{}] ({}) {}".format(obj.__class__.__name__, obj.id,
                                      obj.__dict__)
        out = obj.__str__()
        self.assertEqual(check, out)


if __name__ == '__main__':
    unittest.main()
