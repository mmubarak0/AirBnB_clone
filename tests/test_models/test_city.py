#!/usr/bin/env python3
"""Tests for the city model."""

import unittest
import datetime
from models.base_model import BaseModel
from models.city import City


class TestCityClass(unittest.TestCase):
    """Test city class."""

    def test_0(self):
        """Test name attribute."""
        a = City()
        self.assertEqual(type(a.name), str)

    def test_1(self):
        """Test state_id attribute."""
        a = City()
        self.assertEqual(type(a.state_id), None)
