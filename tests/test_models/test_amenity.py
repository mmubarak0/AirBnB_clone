#!/usr/bin/env python3
"""Tests for the amenity model."""

import unittest
import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """Test amenity class."""

    def test_0(self):
        """Test name attribute."""
        a = Amenity()
        self.assertEqual(type(a.name), str)
