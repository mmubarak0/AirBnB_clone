#!/usr/bin/env python3
"""Tests for the state model."""

import unittest
import datetime
from models.base_model import BaseModel
from models.state import State


class TestStateClass(unittest.TestCase):
    """Test state class."""

    def test_0(self):
        """Test name attribute."""
        a = State()
        self.assertNotEqual(a.name, None)
