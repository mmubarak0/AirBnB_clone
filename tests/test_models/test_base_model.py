#!/usr/bin/env python3
"""Tests for the base model."""

import unittest
import datetime
from models.base_model import BaseModel


class TestBaseClass(unittest.TestCase):
    """Test base class."""

    @classmethod
    def setUpClass(self):
        """Set test class."""
        self.model_1 = BaseModel()
        self.model_2 = BaseModel()
        self.model_3 = BaseModel()
        self.model_4 = BaseModel()
        self.model_5 = BaseModel()
        self.model_6 = BaseModel()

        self.model_5.name = "My First Model"
        self.model_5.my_number = 89
        self.model_5.save()

    def test_0(self):
        """Inequality of two different objects ids."""
        self.assertNotEqual(self.model_1.id, self.model_2.id)
        self.assertNotEqual(self.model_1.id, self.model_3.id)
        self.assertNotEqual(self.model_1.id, self.model_4.id)
        self.assertNotEqual(self.model_1.id, self.model_5.id)
        self.assertNotEqual(self.model_1.id, self.model_6.id)

    def test_1(self):
        """Inequality of more than 2 different objects ids."""
        self.assertNotEqual(self.model_1.id, self.model_2.id)
        self.assertNotEqual(self.model_2.id, self.model_3.id)
        self.assertNotEqual(self.model_3.id, self.model_4.id)
        self.assertNotEqual(self.model_4.id, self.model_5.id)
        self.assertNotEqual(self.model_5.id, self.model_6.id)

    def test_2(self):
        """Check if the id is string."""
        self.assertEqual(type(self.model_1.id), str)
        self.assertEqual(type(self.model_2.id), str)
        self.assertEqual(type(self.model_3.id), str)
        self.assertEqual(type(self.model_4.id), str)
        self.assertEqual(type(self.model_5.id), str)
        self.assertEqual(type(self.model_6.id), str)

    def test_3(self):
        """Check if the BaseModel originates from object class."""
        self.assertTrue(isinstance(BaseModel, object))
        self.assertTrue(isinstance(self.model_1, object))
        self.assertTrue(isinstance(self.model_1, BaseModel))

    def test_4(self):
        """Check if the printing the instance of BaseModel."""
        # match the [<class name>] part
        s = r"\[\w*\]\s"
        # match (<self.id>) part
        s += r"\([a-z0-9]+-[a-z0-9]+-[a-z0-9]+-[a-zA-Z0-9]+-[a-z0-9]+\)\s"
        # match <self.__dict__> part
        s += r"{[^}]*}"

        r = str(self.model_5)
        self.assertRegex(r, s)  # r.search(s)

    def test_5(self):
        """Check the inequality of created_at and updated_at."""
        self.assertEqual(self.model_1.created_at, self.model_1.updated_at)
        self.model_1.save()
        self.assertLess(self.model_1.created_at, self.model_1.updated_at)

    def test_6(self):
        """Check the inequality of updated_at and updated_at."""
        self.model_2.save()
        a = self.model_2.updated_at
        self.model_2.save()
        b = self.model_2.updated_at
        self.assertLess(a, b)

    def test_7(self):
        """Check if the created time is always less than current time."""
        self.assertLess(self.model_1.created_at, datetime.datetime.now())

    def test_8(self):
        """Ensure id is uuid4 (len == 36)."""
        self.assertEqual(len(self.model_5.id), 36)

    def test_9(self):
        """Ensure that method to_dict work fine."""
        test_dict = self.model_5.to_dict()
        self.assertTrue(type(test_dict) is dict)
        # match date.
        s = r"\d{4}-\d{2}-\d{1,2}T"
        # match time.
        s += r"\d{2}:\d{2}:\d{1,2}.\d*"
        r = test_dict["created_at"]
        self.assertRegex(r, s)
        r = test_dict["updated_at"]
        self.assertRegex(r, s)

        self.assertTrue(type(test_dict["id"]) is str)
        self.assertTrue(type(test_dict["created_at"]) is str)
        self.assertTrue(type(test_dict["updated_at"]) is str)

    def test_10(self):
        """Test the usage of kwargs."""
        test_dict = self.model_5.to_dict()
        model_7 = BaseModel(**test_dict)
        self.assertTrue(type(model_7) is BaseModel)
        self.assertTrue(type(model_7.created_at) is datetime.datetime)
        self.assertTrue(type(model_7.updated_at) is datetime.datetime)
        self.assertEqual(model_7.id, self.model_5.id)
        self.assertEqual(model_7.created_at, self.model_5.created_at)
        self.assertEqual(model_7.updated_at, self.model_5.updated_at)
        self.assertEqual(model_7.name, self.model_5.name)
        self.assertEqual(model_7.my_number, self.model_5.my_number)
