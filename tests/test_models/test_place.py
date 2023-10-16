#!/usr/bin/env python3
"""Tests for the place model."""

import unittest
import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """Test place class."""

    def test_0(self):
        """Test city_id attribute."""
        a = Place()
        self.assertEqual(type(a.city_id), str)

    def test_1(self):
        """Test user_id attribute."""
        a = Place()
        self.assertEqual(type(a.user_id), str)

    def test_2(self):
        """Test name attribute."""
        a = Place()
        self.assertEqual(type(a.name), str)

    def test_3(self):
        """Test description attribute."""
        a = Place()
        self.assertEqual(type(a.description), str)

    def test_4(self):
        """Test number_rooms attribute."""
        a = Place()
        self.assertEqual(type(a.number_rooms), int)

    def test_5(self):
        """Test number_bathrooms attribute."""
        a = Place()
        self.assertEqual(type(a.number_bathrooms), int)

    def test_6(self):
        """Test max_guest attribute."""
        a = Place()
        self.assertEqual(type(a.max_guest), int)

    def test_7(self):
        """Test price_by_night attribute."""
        a = Place()
        self.assertEqual(type(a.price_by_night), int)

    def test_8(self):
        """Test latitude attribute."""
        a = Place()
        self.assertEqual(type(a.latitude), float)

    def test_9(self):
        """Test longitude attribute."""
        a = Place()
        self.assertEqual(type(a.longitude), float)

    def test_10(self):
        """Test amenities attribute."""
        a = Place()
        self.assertEqual(type(a.amenities), list)
