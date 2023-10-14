#!/usr/bin/env python3
"""Tests for the storage model."""

import unittest
import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestStorageClass(unittest.TestCase):
    """Test storage class."""
    
    def test_0(self):
        """Test Filestorage."""
        u = FileStorage()
        a = BaseModel()
        u.new(a)
        self.assertTrue(type(u.all()) is dict)
