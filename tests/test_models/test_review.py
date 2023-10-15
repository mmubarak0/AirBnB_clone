#!/usr/bin/env python3
"""Tests for the base model."""

import unittest
import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """Test base class."""

    def test_0(self):
        """Test amenity."""
        a = Review()
        self.assertEqual(len(a.id), 36)
