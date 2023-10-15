#!/usr/bin/python3
"""
test module for Review class
"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    class tests the State class which inherits from BaseModel
    """

    def setUp(self):
        """
        Is executed first before any other tests
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
        tests if the class is instantiated and inherits correctly
        """
        obj = Review()
        self.assertIsInstance(obj, Review)
        self.assertIsInstance(obj, BaseModel)
        # instantiate with argument
        obj = Review(45)
        self.assertIsInstance(obj, Review)
        self.assertFalse(hasattr(obj, "45"))

    def test_init_kwargs(self):
        """
        pass key worded arguments as parameters
        """

        obj = Review(name="Isaiah")
        self.assertIsInstance(obj, Review)

        # multiple arguments
        obj = Review(name="Isaiah", name2="Kipyego")

    def test_attributes(self):
        """
        test if main class Attributes exist
        """
        obj = Review()
        self.assertIsInstance(obj, Review)
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "__class__"))
        self.assertFalse(hasattr(obj, "Isaiah"))
        self.assertTrue(hasattr(obj, "place_id"))
        self.assertTrue(hasattr(obj, "user_id"))
        self.assertTrue(hasattr(obj, "text"))

    def test_to_dict(self):
        """
        test the inherited to dict method
        """
        obj_1 = Review()
        obj_2 = Review()
        test = obj_1.to_dict()
        self.assertIsInstance(obj_1, Review)
        self.assertEqual(type(obj_1).__name__, "Review")
        self.assertEqual(test['__class__'], "Review")
        self.assertTrue(type(test['created_at']), 'str')
        self.assertNotEqual(obj_1.id, obj_2.id)

    def test_str(self):
        """
        test if the __str__ method is working as expected
        """
        obj = Review()
        check = "[{}] ({}) {}".format(obj.__class__.__name__, obj.id,
                                      obj.__dict__)
        out = obj.__str__()
        self.assertEqual(check, out)


if __name__ == '__main__':
    unittest.main()
