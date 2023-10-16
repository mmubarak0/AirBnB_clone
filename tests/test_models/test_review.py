#!/usr/bin/env python3
"""Tests for the review model."""

import unittest
import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """Test review class."""

    def test_0(self):
        """Test place_id attribute."""
        a = Review()
        self.assertEqual(type(a.place_id), str)

    def test_0(self):
        """Test user_id attribute."""
        a = Review()
        self.assertEqual(type(a.user_id), str)

    def test_0(self):
        """Test text attribute."""
        a = Review()
        self.assertEqual(type(a.text), str)
