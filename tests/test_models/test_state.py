#!/usr/bin/python3
"""
test module for State class
"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    class tests the State class which inherits from BaseModel
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
        executed last after all tests have been performed
        """
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_init(self):
        """
        tests if the class is instantiated and inherits correctly
        """
        obj = State()
        self.assertIsInstance(obj, State)
        self.assertIsInstance(obj, BaseModel)
        # instantiate with argument
        obj = State(45)
        self.assertIsInstance(obj, State)
        self.assertFalse(hasattr(obj, "45"))

    def test_init_kwargs(self):
        """
        pass key worded arguments as parameters
        """

        obj = State(name="Isaiah")
        self.assertIsInstance(obj, State)

        # multiple arguments
        obj = State(name="Isaiah", name2="Kipyego")

    def test_attributes(self):
        """
        test if main class Attributes exist
        """
        obj = State()
        self.assertIsInstance(obj, State)
        self.assertTrue(hasattr(obj, "name"))
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "__class__"))
        self.assertFalse(hasattr(obj, "Isaiah"))

    def test_to_dict(self):
        """
        test inherited to dict method
        """
        obj_1 = State()
        obj_2 = State()
        test = obj_1.to_dict()
        self.assertIsInstance(obj_1, State)
        self.assertEqual(type(obj_1).__name__, "State")
        self.assertEqual(test['__class__'], "State")
        self.assertTrue(type(test['created_at']), 'str')
        self.assertNotEqual(obj_1.id, obj_2.id)

    def test_str(self):
        """
        test if __str__ method is working as expected
        """
        obj = State()
        check = "[{}] ({}) {}".format(obj.__class__.__name__, obj.id,
                                      obj.__dict__)
        out = obj.__str__()
        self.assertEqual(check, out)


if __name__ == '__main__':
    unittest.main()
