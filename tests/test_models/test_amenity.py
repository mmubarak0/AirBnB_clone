#!/usr/bin/env python3
"""Tests for the base model."""

import unittest
import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """Test base class."""

    def test_0(self):
        """Test amenity."""
        a = Amenity()
        self.assertEqual(len(a.id), 36)
