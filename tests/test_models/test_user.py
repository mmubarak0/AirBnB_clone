#!/usr/bin/env python3
"""Tests for the user model."""

import unittest
import datetime
from models.base_model import BaseModel
from models.user import User


class TestUserClass(unittest.TestCase):
    """Test user class."""

    def test_0(self):
        """Test email attribute."""
        a = User()
        self.assertEqual(type(a.email), str)

    def test_1(self):
        """Test password attribute."""
        a = User()
        self.assertEqual(type(a.password), str)

    def test_2(self):
        """Test first_name attribute."""
        a = User()
        self.assertEqual(type(a.first_name), str)

    def test_3(self):
        """Test last_name attribute."""
        a = User()
        self.assertEqual(type(a.last_name), str)
