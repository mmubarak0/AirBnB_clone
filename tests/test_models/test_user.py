#!/usr/bin/env python3
"""Tests for the base model."""

import unittest
import datetime
from models.base_model import BaseModel
from models.user import User


class TestUserClass(unittest.TestCase):
    """Test base class."""

    def test_0(self):
        """Test amenity."""
        a = User()
        self.assertEqual(len(a.id), 36)
